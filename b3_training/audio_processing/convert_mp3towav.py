import numpy as np
import librosa
import soundfile as sf
from glob import glob
import os
import warnings
warnings.simplefilter('ignore')

####### convert .mp3 data in "mp3_data" to .wav data and save to "wav_data/input"
####### "mp3_data"内のデータを .wav形式に変換して"wav_data/input"に保存する．
mp3_dir = "mp3_data"
wav_save_dir = "wav_data" + os.sep + "input"

####### if "", convert all files in "mp3_data"
####### 変換したいファイル名を入れれば，そのファイルだけ変換
mp3_filenames = []
# mp3_filenames = ["hoge.mp3", "hogehoge.mp3"]

####### maximum length[sec.] of .wav
####### .mp3 が長すぎた場合この長さ[秒]でカットして .wavを出力
max_length = 30


if len(mp3_filenames) == 0:
    ###### get all data of .mp3
    files = glob(mp3_dir + os.sep + "*.mp3")
    for file in files:
        ####### pick filename by end of splitted file and append
        mp3_filenames.append(file.split(os.sep)[-1])
else:
    files = []
    ####### only in mp3_filenames
    for filename in mp3_filenames:
        files.append(mp3_dir + os.sep + filename)


for file, filename in zip(files, mp3_filenames):
    ####### output filename(suffix changed)
    output_file = wav_save_dir + os.sep + filename[:-4] + ".wav"
    wave, sr = librosa.core.load(file)
    sf.write(output_file, wave[:max_length*sr], sr, format="wav")
    print(f"Converted {filename} to WAV")
