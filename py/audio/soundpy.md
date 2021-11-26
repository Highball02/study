# INSTALL  
sudo apt install portaudio19-dev  
pip3 install pyaudio  
/usr/local/bin/python3.9 -m pip install --upgrade pip  #pipを3.6から3.9に対応させた  
pip3 install matplotlib


# PYAUDIO  
chunk 読み込む際のデータサイズ 1024*nにすることが多い  usbマイクは以上でできた4096
rate サンプリングレート 44100hz=44.1khz  
