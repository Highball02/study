import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

print(p.is_format_supported(44100,12,1,pyaudio.paInt16))
p.terminate()
## default PC mic index=21  name default maxinputChannels=32