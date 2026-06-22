# 录音转文字能力留存

这套录音转文字能力已经集中放在这个文件夹里：

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\audio-transcription`

## 入口

脚本文件：

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\audio-transcription\transcribe_audio.py`

双击入口：

`C:\Users\yelin01\Documents\Codex\2026-06-15\new-chat-4\audio-transcription\transcribe_audio.bat`

## 用法

命令行运行：

```powershell
& 'C:\Users\yelin01\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' .\audio-transcription\transcribe_audio.py "C:\路径\你的录音.m4a"
```

也可以把录音文件直接拖到 `transcribe_audio.bat` 上运行。

运行后会在录音同目录下生成：

`录音文件名_transcript.txt`

## 当前目录结构

- `transcribe_audio.py`：主转写脚本
- `transcribe_audio.bat`：双击或拖拽启动入口
- `vosk-model-small-cn-0.22/`：本地中文识别模型
- `sample-audio/`：示例音频
- `sample-output/`：示例转写结果

## 说明

这套能力适合先快速出一版逐段文字稿。口语、专有名词、人名较多时，识别结果通常还需要再顺一遍。
