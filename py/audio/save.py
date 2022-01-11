import pyaudio
import wave

chunk = 1024*4
CHANNELS = 1 #1:モノラル 2:ステレオ
RATE = 44100  # サンプリングレート
FORMAT = pyaudio.paInt16
#print("Record seconds? ")
RECORD_SECONDS = 5   #int(input())

p = pyaudio.PyAudio()
# 録音開始

print("rec start")
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,output=False,
                input=True, frames_per_buffer=chunk,input_device_index=12)
 
outdata = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    outdata.append(data)

stream.stop_stream()
stream.close()  # 録音終了
print("rec end")
SAMPLWIDTH=p.get_sample_size(FORMAT)
p.terminate()
   
outdata = b''.join(outdata)

out = wave.open('sampl.wav', 'wb')
out.setnchannels(CHANNELS)
out.setsampwidth(SAMPLWIDTH)
out.setframerate(RATE)
out.writeframes(outdata)
out.close()
#del out
#print(p.is_format_supported(44100,12,1,pyaudio.paInt8))
