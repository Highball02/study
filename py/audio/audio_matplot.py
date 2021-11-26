import pyaudio
import numpy
import matplotlib.pyplot as plt

chunk = 4096
FORMAT = pyaudio.paInt16 #int型16bit

CHANNELS = 1 #モノラル（2にするとステレオ）
RATE = 44100 #サンプルレート（録音の音質）
RECORD_SECONDS = 5 #録音時間(s)

p = pyaudio.PyAudio() #インスタンス生成

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True, 
                frames_per_buffer = chunk,
                input_device_index=12)  # 録音開始（）内で設定
#input_device_index = 1,  #録音デバイス設定
#レコード開始
print("Now Recording...")
data = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    stream_data = stream.read(chunk) #音声を読み取って、
    data.append(stream_data) #データを追加


print("Finished Recording.")

stream.close()#レコード終了
p.terminate()

#data = ''.join(data) #Python2用
data = b"".join(data) #Python3用

#録音したデータを配列に変換
result = numpy.frombuffer(data,dtype="int16") / float(2**15)

plt.plot(result)
plt.show()