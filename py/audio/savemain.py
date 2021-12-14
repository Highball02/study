
from typing import FrozenSet
import pyaudio
import wave
import numpy as np
import time
#from concurrent.futures import ThreadPoolExecutor


chunk = 4096
FORMAT = pyaudio.paInt16  # int型16bits
CHANNELS = 1  # モノラル（2にするとステレオ）
RATE = 44100  # サンプルレート（録音の音質）
RECORD_SECONDS = 5  # 録音時間(s)

mic1_index = 12  # マイク1  usb
mic2_index = 18  # マイク2  PC default

s_data = []
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk,
                input_device_index=12)


start = time.time()
print("start")
while stream.is_active() and time.time() - start < 5:
    data = stream.read(chunk)
    s_data.append(data)


stream.stop_stream()
stream.close()
p.terminate()

data = b' '.join(s_data)

with wave.open('samp.wav', 'wb') as out:
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(RATE)
    out.writeframes(data)

print("Stop Streaming")
