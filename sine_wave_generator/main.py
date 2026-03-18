import os
import numpy as np
from tone import Tone

def generate_signal(duration=3.0):
    """
    Generates and returns the raw numpy array containing the synthesized sound segment.
    """
    alpha = 2 * np.pi * 2   # 2 Hz gating
    beta  = 2 * np.pi * 1   # 1 Hz gating
    gamma = 2 * np.pi * 440 # 440 Hz tone
    delta = 2 * np.pi * 880 # 880 Hz tone

    s_t = Tone.get_sound_segment_signal(alpha, beta, gamma, delta, duration=duration)
    return s_t

if __name__ == "__main__":
    alpha = 2 * np.pi * 2
    beta  = 2 * np.pi * 1
    gamma = 2 * np.pi * 440
    delta = 2 * np.pi * 880
    
    print("Playing generated sound segment...")
    Tone.sound_segment(alpha, beta, gamma, delta, duration=3)