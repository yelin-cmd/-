from __future__ import annotations

import argparse
import json
import subprocess
import sys
import wave
from pathlib import Path

from vosk import KaldiRecognizer, Model, SetLogLevel


WORKSPACE_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL_DIR = WORKSPACE_DIR / "vosk-model-small-cn-0.22"
DEFAULT_FFMPEG_PATH = Path(r"C:\Program Files\EVCapture\ffmpeg.exe")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file to timestamped text using a local Vosk model."
    )
    parser.add_argument("input", help="Path to the source audio file.")
    parser.add_argument(
        "-o",
        "--output",
        help="Path to the output text file. Defaults to <input>_transcript.txt.",
    )
    parser.add_argument(
        "--model-dir",
        default=str(DEFAULT_MODEL_DIR),
        help=f"Path to the Vosk model directory. Defaults to {DEFAULT_MODEL_DIR}.",
    )
    parser.add_argument(
        "--ffmpeg",
        default=str(DEFAULT_FFMPEG_PATH),
        help=f"Path to ffmpeg.exe. Defaults to {DEFAULT_FFMPEG_PATH}.",
    )
    return parser.parse_args()


def ensure_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")


def format_ts(seconds: float) -> str:
    total = int(seconds)
    minutes, secs = divmod(total, 60)
    return f"{minutes:02d}:{secs:02d}"


def convert_to_wav(input_path: Path, wav_path: Path, ffmpeg_path: Path) -> None:
    ensure_exists(ffmpeg_path, "ffmpeg")
    command = [
        str(ffmpeg_path),
        "-y",
        "-i",
        str(input_path),
        "-ar",
        "16000",
        "-ac",
        "1",
        "-f",
        "wav",
        str(wav_path),
    ]
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "ffmpeg conversion failed")


def transcribe_wav(wav_path: Path, model_dir: Path) -> list[str]:
    ensure_exists(model_dir, "Model directory")

    with wave.open(str(wav_path), "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            raise RuntimeError("WAV file must be mono PCM.")

        SetLogLevel(-1)
        model = Model(str(model_dir))
        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetWords(True)

        results: list[dict] = []
        while True:
            data = wf.readframes(4000)
            if not data:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                if result.get("text"):
                    results.append(result)

        final_result = json.loads(recognizer.FinalResult())
        if final_result.get("text"):
            results.append(final_result)

    lines: list[str] = []
    for result in results:
        text = result.get("text", "").strip()
        words = result.get("result") or []
        if not text:
            continue
        if words:
            start = format_ts(words[0]["start"])
            end = format_ts(words[-1]["end"])
            lines.append(f"[{start}-{end}] {text}")
        else:
            lines.append(text)
    return lines


def build_output_path(input_path: Path, output_arg: str | None) -> Path:
    if output_arg:
        return Path(output_arg).expanduser().resolve()
    return input_path.with_name(f"{input_path.stem}_transcript.txt")


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = build_output_path(input_path, args.output)
    model_dir = Path(args.model_dir).expanduser().resolve()
    ffmpeg_path = Path(args.ffmpeg).expanduser().resolve()

    ensure_exists(input_path, "Input audio")

    temp_wav_path = output_path.with_suffix(".tmp.wav")
    try:
        convert_to_wav(input_path, temp_wav_path, ffmpeg_path)
        lines = transcribe_wav(temp_wav_path, model_dir)
        output_path.write_text("\n".join(lines), encoding="utf-8")
    finally:
        if temp_wav_path.exists():
            temp_wav_path.unlink()

    print(f"Transcript saved to: {output_path}")
    print(f"Line count: {len(lines)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
