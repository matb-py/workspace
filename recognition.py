import speech_recognition as sr

r = sr.Recognizer()

#AudioFileの引数には、wav形式のファイルを設定する
with sr.AudioFile('C:\\Users\\matb0\\Downloads\\001-sibutomo (1).wav') as src:
    audio = r.record(src)
print(r.recognize_google(audio, language='ja-JP'))