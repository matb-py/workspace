#音声入力をwavファイルに出力する
#参考：
#https://people.csail.mit.edu/hubert/pyaudio/
#https://people.csail.mit.edu/hubert/pyaudio/docs/#pyaudio.Stream.__init__
#https://algorithm.joho.info/programming/python/pyaudio-device-index/
#https://algorithm.joho.info/programming/python/pyaudio-record/
#pyaudioのインストール失敗した場合：https://education.r-jc.jp/?p=1989

import pyaudio  #オーディオI/Oライブラリ
import wave     #wavファイルを扱うためのライブラリ
 
WAVE_OUTPUT_FILENAME = "sample.wav" #音声を保存するファイル名
 
def CreateWavFile(Record_Seconds):

    CHUNK = 1024             # チャンク（データ点数）
    FORMAT = pyaudio.paInt16 # int16型
    CHANNELS = 2             # ステレオ（1：モノラル）
    RATE = 44100             # サンプルレート（録音の音質）
    INDEX = 1                # 録音デバイスのインデックス番号（デフォルト1）
    
    p = pyaudio.PyAudio()


#    もし、音声が拾えない場合は、コメントを外してオーディオデバイスを確認
#    使用可能なデバイスをインデックス番号に指定する
#    for x in range(0, p.get_device_count()): 
#       print(p.get_device_info_by_index(x))

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    output  = False,
                    input_device_index = INDEX,
                    frames_per_buffer = CHUNK)
    
    #レコード開始
    print("----開始----")
    all = []
    for i in range(0, int(RATE / CHUNK * Record_Seconds)):
        data = stream.read(CHUNK) #音声を読み取って、
        all.append(data) #データを追加
    
    #レコード終了
    print("----終了----")
    
    stream.close()
    p.terminate()
    wavFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wavFile.setnchannels(CHANNELS)
    wavFile.setsampwidth(p.get_sample_size(FORMAT))
    wavFile.setframerate(RATE)
    wavFile.writeframes(b''.join(all))
    
    wavFile.close()


#実行
#引数：５秒
CreateWavFile(5)
