import os
from tone import Tone
import numpy as np

# Example: 440Hz and 880Hz tones gated at 2Hz and 1Hz respectively
alpha = 2 * np.pi * 2   # 2 Hz gating
beta  = 2 * np.pi * 1   # 1 Hz gating
gamma = 2 * np.pi * 440 # 440 Hz tone
delta = 2 * np.pi * 880 # 880 Hz tone

# Path to save the WAV file in libnmfd/data
output_file = os.path.abspath("../libnmfd/data/sound_segment.wav")

print(f"Generating sound segment and saving to {output_file}...")
Tone.sound_segment(alpha, beta, gamma, delta, duration=3, filename=output_file)
