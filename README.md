# Local Audio Transcription

一个本地离线的录音转文字小工具，适合快速把 `m4a`、`wav` 等音频转成带时间戳的中文文本稿。

## Included Files

- `transcribe_audio.py`: 主转写脚本
- `transcribe_audio.bat`: Windows 双击/拖拽启动入口
- `README_transcription.md`: 中文使用说明
- `.gitignore`: 忽略模型、录音和转写结果等大文件

## Quick Start

```powershell
& 'C:\Users\yelin01\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\transcribe_audio.py "C:\path\to\audio.m4a"
```

输出文件默认生成在原录音同目录下，命名为：

`原文件名_transcript.txt`

## Notes

- 使用本地 `Vosk` 中文模型离线识别
- 依赖 `ffmpeg` 把输入音频转成识别所需的 WAV 格式
- 更适合先出初稿，专有名词和口语内容建议人工顺稿
