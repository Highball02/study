import pyaudio
import wave

chunk = 1024*4
CHANNELS = 1 #モノラル
RATE = 44100  # サンプリングレート
FORMAT = pyaudio.paInt16

#print("Record seconds? ")
RECORD_SECONDS = 3   #int(input())

p = pyaudio.PyAudio()
# 録音開始
print("start")
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,output=True,
                input=True, frames_per_buffer=chunk,input_device_index=12)
 
s_data = []
for i in range(0, int(RATE/chunk*RECORD_SECONDS)):
    data = stream.read(chunk)
    s_data.append(data)

stream.close()  # 録音終了
print("end")
p.terminate()
   
s_data = b' '.join(s_data)

out = wave.open('sampl.wav', 'w')
out.setnchannels(2)
out.setsampwidth(2)
out.setframerate(RATE)
out.writeframes(s_data)
out.close()
del out
print(p.is_format_supported(44100,12,1,pyaudio.paInt16))
