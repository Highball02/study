import pyaudio
soundObj = pyaudio.PyAudio()

# Learn what your OS+Hardware can do  ####
#defaultCapability = soundObj.get_default_host_api_info()
#print(defaultCapability)

# See if you can make it do what you want
isSupported = soundObj.is_format_supported(input_format=pyaudio.paInt16, input_channels=2, rate=1024*100,input_device=12,)
print(isSupported) 