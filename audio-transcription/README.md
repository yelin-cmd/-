# Local Audio Transcription

An offline audio-to-text tool for quickly turning `m4a`, `wav`, and similar audio files into timestamped Chinese transcripts.

## Folder

All transcription assets are kept in:

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\audio-transcription`

## Included Files

- `transcribe_audio.py`: main transcription script
- `transcribe_audio.bat`: double-click or drag-and-drop launcher for Windows
- `README_transcription.md`: Chinese usage guide
- `vosk-model-small-cn-0.22/`: local Chinese speech model
- `sample-audio/`: sample input audio
- `sample-output/`: sample transcript output

## Quick Start

```powershell
& 'C:\Users\yelin01\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\audio-transcription\transcribe_audio.py "C:\path\to\audio.m4a"
```

You can also drag an audio file onto `transcribe_audio.bat`.

## Notes

- Uses a local `Vosk` Chinese model for offline recognition
- Relies on `ffmpeg` to convert source audio into recognition-ready WAV
- Best for generating a first-pass transcript; spoken filler, names, and domain terms may need manual cleanup
