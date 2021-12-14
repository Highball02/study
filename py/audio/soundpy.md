# INSTALL  
sudo apt install portaudio19-dev  
pip3 install pyaudio  
/usr/local/bin/python3.9 -m pip install --upgrade pip  #pipを3.6から3.9に対応させた  
pip3 install matplotlib


# PYAUDIO  
chunk 読み込む際のデータサイズ 1024*nにすることが多い  usbマイクは4096以上でできた
rate サンプリングレート 44100hz=44.1khz  


# memo
alsa のエラー？    /usr/share/alsa/
gdb で動作確認 stream2をオープンした直後にダンプ

