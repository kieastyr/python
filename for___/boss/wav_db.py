import wave
import os

data_path = os.listdir('wavdata')
#とりあえずwavdataディレクトリ内の最初のwavデータを習得
waveFile = wave.open('wavdata'+os.sep+data_path[0],'r')
buf = waveFile.readframes(-1)
waveFile.close()

