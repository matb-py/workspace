#Windows限定
#pip install pywin32
import win32com.client as win
voice = win.Dispatch("SAPI.SpVoice")
voice.Volume=50
voice.Rate=5
voice.Speak("キアヌ・チャールズ・リーブス")
voice.Volume=100
voice.Rate=5
voice.Speak("俳優。レバノンで生まれ、カナダのトロントで育った。")
voice.Speak("『スピード』や『マトリックス』シリーズ、『ジョン・ウィック』シリーズの主演で知られる。")
#print("何をしゃべらせますか？ ", end="")
#message = input()
#voice.Speak(message)
