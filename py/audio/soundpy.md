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



# mic check
{'index': 12, 'structVersion': 2, 'name': 'USB PnP Sound Device: Audio (hw:2,0)', 'hostApi': 0, 'maxInputChannels': 1, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.008684807256235827, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.034829931972789115, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 44100.0}
{'index': 13, 'structVersion': 2, 'name': 'USB PnP Sound Device: Audio (hw:3,0)', 'hostApi': 0, 'maxInputChannels': 1, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.008684807256235827, 'defaultLowOutputLatency': -1.0, 'defaultHighInputLatency': 0.034829931972789115, 'defaultHighOutputLatency': -1.0, 'defaultSampleRate': 44100.0}





# report
目的
ゴール
結果まとめ　2行ぐらいで完結に
結果
この技術でビジネスするなら
A4一枚＋添付資料


