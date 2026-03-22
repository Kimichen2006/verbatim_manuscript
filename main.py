# 安裝必要套件：OpenAI Whisper 與 YouTube 下載工具
#!pip install -U openai-whisper yt-dlp -q
# 安裝系統依賴 ffmpeg (Whisper 處理音訊必備)
#!apt update && apt install ffmpeg -y -q

import whisper
import os
import subprocess

# 設定 YouTube 網址
youtube_url = input("輸入網址: ")

# 使用 yt-dlp 下載影片的音訊部分
print("正在從 YouTube 下載音訊...")
audio_filename = "yt_audio.mp3"
# 如果檔案已存在則先刪除
if os.path.exists(audio_filename):
    os.remove(audio_filename)

# 執行下載指令，僅擷取音訊並轉換為 mp3
download_cmd = f'yt-dlp -x --audio-format mp3 -o "{audio_filename}" {youtube_url}'
subprocess.run(download_cmd, shell=True)

if os.path.exists(audio_filename):
    print("音訊下載成功，開始載入 Whisper 模型進行辨識...")

    # 載入 Whisper 模型 (模型大小可選: tiny, base, small, medium, large)
    # medium 是一個平衡速度與準確度的選擇
    model = whisper.load_model("medium")

    # 逐字稿辨識
    print("正在辨識逐字稿 (這可能需要幾分鐘，視影片長度而定)... ")
    result = model.transcribe(audio_filename)

    # 辨識結果
    print("\n--- 辨識結果 ---")
    print(result["text"])

else:
    print("音訊下載失敗，請檢查 URL 是否正確。")
