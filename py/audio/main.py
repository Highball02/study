import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt
import threading


chunk = 4096
FORMAT = pyaudio.paInt16  # int型16bit
CHANNELS = 1  # モノラル（2にするとステレオ）
RATE = 44100  # サンプルレート（録音の音質）
RECORD_SECONDS = 5  # 録音時間(s)

mic1_index = 12  # マイク1  usb
mic2_index = 21  # マイク2  PC default
p = pyaudio.PyAudio()


def save1(rec_sec=3):
    # stream1 start
    stream1 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                     input=True, frames_per_buffer=chunk, input_device_index=mic1_index)

    stream_data1 = []
    for i in range(0, int(RATE/chunk*rec_sec)):
        data1 = stream1.read(chunk)
        stream_data1.append(data1)
    print("stream1 end")
    stream1.close()
    # p.terminate()
    data1 = b" ".join(stream_data1)
    #result1 = np.frombuffer(data1, dtype="int16")/float(2**15)
    # plt.plot(result1)
    # plt.show()
    out = wave.open('sample1.wav', 'w')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(RATE)
    out.writeframes(data1)
    out.close()


def save2(rec_sec=3):
    # stream2 start
    stream2 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
                     frames_per_buffer=1024, input_device_index=mic2_index)  # input_device_index=mic1_index,
    stream_data2 = []
    for i in range(0, int(RATE/chunk*rec_sec)):
        data2 = stream2.read(chunk)
        stream_data2.append(data2)
    print("stream2 end")
    stream2.close()
    # p.terminate()
    data2 = b" ".join(stream_data2)
    #result2 = np.frombuffer(data2, dtype="int16")/float(2**15)
    # plt.plot(result2)
    # plt.show()
    out = wave.open('sample2.wav', 'w')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(RATE)
    out.writeframes(data2)
    out.close()


# th = [threading.Thread(target=save1),
#      threading.Thread(target=save2)]
# for t in th:
#   t.start()
#    t.join()


p.terminate()
t1 = threading.Thread(target=save1)
t2 = threading.Thread(target=save2)
t1.start()
t2.start()
t1.join()
t2.join()
