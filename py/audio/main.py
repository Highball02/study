#import numpy as np
import wave
import pyaudio
#import matplotlib.pyplot as plt
import threading
import time


chunk = 1024*4
FORMAT = pyaudio.paInt16  # int型16bits
CHANNELS = 1  # モノラル（2にするとステレオ）
RATE =44100*1.2  # サンプルレート（録音の音質）
#RECORD_SECONDS = 5  # 録音時間(s)

mic1_index = 12  # マイク1  usb
mic2_index = 13  # マイク2  usb2    18 PC default
p1 = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()

rec_sec = 10


def save1():
    print("stream1 start")
    stream1 = p1.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                      input=True, frames_per_buffer=chunk, input_device_index=mic1_index)
    print("stream1 open")
    stream_data1 = []
    for i in range(0, int(RATE/chunk*rec_sec)):
        data1 = stream1.read(chunk)
        stream_data1.append(data1)
        print("1")
    stream1.stop_stream()
    print("stream1 end")
    stream1.close()
    
    data1 = b" ".join(stream_data1)
    #result1 = np.frombuffer(data1, dtype="int16")/float(2**15)
    # plt.plot(result1)
    # plt.show()
    out1 = wave.open('sample1.wav','wb')
    out1.setnchannels(1)
    out1.setsampwidth(2)
    out1.setframerate(RATE)
    out1.writeframes(data1)
    out1.close()


def save2():
    print("stream2 start")
    stream2 = p2.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,output=False,
                      frames_per_buffer=chunk, input_device_index=mic2_index) 
    print("stream2 open")
    stream_data2 = []
    for j in range(0, int(RATE/chunk*rec_sec)):
        data2 = stream2.read(chunk)
        stream_data2.append(data2)
        print("2")
    stream2.stop_stream()
    print("stream2 end")
    stream2.close()
    
    data2 = b" ".join(stream_data2)
    #result2 = np.frombuffer(data2, dtype="int16")/float(2**15)
    # plt.plot(result2)
    # plt.show()
    out2 = wave.open('sample2.wav', 'wb')
    out2.setnchannels(1)
    out2.setsampwidth(2)
    out2.setframerate(RATE)
    out2.writeframes(data2)
    out2.close()


# th = [threading.Thread(target=save1),
#      threading.Thread(target=save2)]
# for t in th:
#   t.start()
#    t.join()


# p.terminate()
t1 = threading.Thread(target=save1)
t2 = threading.Thread(target=save2)
t1.start()
t2.start()
#time.sleep(5)

