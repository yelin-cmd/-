# 录音转文字能力留存

这个目录里已经留好一套本地可复用的录音转文字能力。

## 入口

脚本文件：

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\transcribe_audio.py`

## 用法

在这个目录里运行：

```powershell
& 'C:\Users\yelin01\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\transcribe_audio.py "C:\路径\你的录音.m4a"
```

运行后会在录音同目录下生成：

`录音文件名_transcript.txt`

## 当前依赖

- 本地识别模型：`vosk-model-small-cn-0.22`
- 音频转换工具：`C:\Program Files\EVCapture\ffmpeg.exe`
- Python 运行时：Codex 自带 Python

## 已验证样例

已用下面这个文件跑通过：

`C:\Users\yelin01\Desktop\20260617_160001.m4a`

输出文件：

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\20260617_160001_transcript.txt`

## 说明

这套能力适合先快速出一版逐段文字稿。口语、专有名词、人名较多时，识别结果可能需要再顺一遍。
