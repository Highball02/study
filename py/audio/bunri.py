#cal
import pyroomacoustics as pr
import scipy.signal as sig
from sklearn.decomposition import PCA
#system
import glob
import numpy as np
#audio
from IPython.display import display, Audio
import scipy.io.wavfile as wav

#パラメータ
data_dir = "audio" #音源wavの入ってるディレクトリ
N = 2 #音源数
RT = 0.3 #室内残響時間

#データ読み込み
data_list = [] #ORIGINAL
for f in glob.glob(data_dir+'/*.wav'):
    RATE,data = wav.read(f)
    data_list.append(data)
t_data = np.stack(data_list, axis=1)


# 主成分分析（PCA）で次元下げ
pca = PCA(n_components=N, whiten=True)
H = pca.fit_transform(t_data)

#STFT()
#STFT窓長を室内残響時間より長くします
n = RT*RATE
i = 1
while ( i * 2 <= n):
    i *= 2
seg = i * 2
stft_list = [] #STFT
for i in range(N):
    _,_,Z = sig.stft(H[:,i],nperseg=seg)
    stft_list.append(Z.T)
f_data = np.stack(stft_list, axis=2)

# ILRMA計算
Array = pr.bss.ilrma(f_data, n_src=None, n_iter=100, proj_back=True, W0=None, n_components=2, return_filters=False, callback=None)

# 出力
sep = [] #ここに音源データが入るので煮るなり焼くなり
for i in range(N):
    x=sig.istft(Array[:,:, -(i+1)].T, nperseg=seg)

    sep.append(x[1])
    display(Audio(x[1], rate=RATE))