import numpy as np
import os
import matplotlib.pyplot as plt
import librosa

load_dir = "dist-data" + os.sep + "noised_tgt"
mel = np.load(load_dir + os.sep + "noised_tgt_001" + ".npy")
wave = librosa.feature.inverse.mfcc_to_audio(mel)
plt.plot(wave)
plt.show()

