import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt

chunk = 1024
FORMAT = pyaudio.paInt16 #int型16bit
CHANNELS = 1 #モノラル（2にするとステレオ）
RATE = 44100 #サンプルレート（録音の音質）
RECORD_SECONDS = 5 #録音時間(s)

mic1_index=1  #マイク1
mic2_index=2  #マイク2

def save1():
    p=pyaudio.PyAudio()

    #stream1 start
    stream1=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=chunk)#input_device_index=mic1_index,

    all=[]
    for i in range(0,int(RATE/chunk*RECORD_SECONDS)):
        data1=stream1.read(chunk)
        all.append(data1)
    #stream1 end
    stream1.close()
    p.terminate()

    data1=b"".join(all)
    result1=np.frombuffer(data1,dtype="int16")/float(2**15)
    plt.plot(result1)
    plt.show()




def save2():
    p=pyaudio.PyAudio()

    #stream2 start
    stream2=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=chunk)#input_device_index=mic1_index,

    all=[]
    for i in range(0,int(RATE/chunk*RECORD_SECONDS)):
        data2=stream2.read(chunk)
        all.append(data2)
    #stream2 end
    stream2.close()
    p.terminate()

    data2=b"".join(all)
    result2=np.frombuffer(data2,dtype="int16")/float(2**15)
    plt.plot(result2)
    plt.show()

    save1()
    save2()

