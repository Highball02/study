import pyaudio
import wave

chunk=1024
CHANNELS=1
RATE=44100 #サンプリングレート 
FORMAT=pyaudio.paInt16

print("Record seconds? ")
RECORD_SECONDS=int(input())

p=pyaudio.PyAudio()
#録音開始
print("start")
stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=chunk)

all=[]
for i in range(0,int(RATE/chunk*RECORD_SECONDS)):
    data=stream.read(chunk)
    all.append(data)

stream.close()#録音終了
print("end")
p.terminate()

data=b''.join(all)

out = wave.open('sample.wav','w')
out.setnchannels(1)
out.setsampwidth(2)
out.setframerate(RATE)
out.writeframes(data)
out.close()
