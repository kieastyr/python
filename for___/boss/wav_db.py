import wave
import os

data_path = os.listdir('wavdata')
#�Ƃ肠����wavdata�f�B���N�g�����̍ŏ���wav�f�[�^���K��
waveFile = wave.open('wavdata'+os.sep+data_path[0],'r')
buf = waveFile.readframes(-1)
waveFile.close()

