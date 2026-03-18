import pygame
import numpy
import math
import time

pygame.init()

bits = 16
sample_rate = 44100 #bits per second
pygame.mixer.pre_init(sample_rate, bits)

def sine_x (amp, freq, time):
    return int(round (amp * math.sin(2 * math.pi * freq * time)))


import scipy.io.wavfile
import os

class Tone:
    @staticmethod
    def _create_buffer(signal, speaker=None):
        """
        Helper to create a stereo buffer from a 1D signal.
        """
        num_sample = len(signal)
        sound_buffer = numpy.zeros((num_sample, 2), dtype=numpy.int16)

        if speaker == "r":
            sound_buffer[:, 1] = signal
        elif speaker == "l":
            sound_buffer[:, 0] = signal
        else:
            sound_buffer[:, 0] = signal
            sound_buffer[:, 1] = signal
        
        return sound_buffer

    @staticmethod
    def save_wav(buffer, filename):
        """
        Saves the audio buffer to a WAV file.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        scipy.io.wavfile.write(filename, sample_rate, buffer)
        print(f"Saved sound to: {filename}")

    @staticmethod
    def sine(freq, duration=1, speaker=None, filename=None):
        """
        Generates and plays/saves a simple sine wave tone.
        """
        num_sample = int(round(duration * sample_rate))
        amplitude = 2 ** (bits - 1) - 1
        
        t = numpy.linspace(0, duration, num_sample, endpoint=False)
        wave = (amplitude * numpy.sin(2 * numpy.pi * freq * t)).astype(numpy.int16)

        sound_buffer = Tone._create_buffer(wave, speaker)

        if filename:
            Tone.save_wav(sound_buffer, filename)
        else:
            sound = pygame.sndarray.make_sound(sound_buffer)
            sound.play(loops=0, maxtime=int(duration * 1000))
            time.sleep(duration)

    @staticmethod
    def sound_segment(alpha, beta, gamma, delta, duration=1, speaker=None, filename=None):
        """
        Implementation of the sound segment formula (3):
        s(t) = g(alpha * t) * sin(gamma * t) + g(beta * t) * sin(delta * t)
        """
        num_sample = int(round(duration * sample_rate))
        amplitude = 2 ** (bits - 1) - 1
        
        t = numpy.linspace(0, duration, num_sample, endpoint=False)
        
        def g(x):
            return (numpy.mod(x, 2 * numpy.pi) < numpy.pi).astype(numpy.float32)
        
        s_t = g(alpha * t) * numpy.sin(gamma * t) + g(beta * t) * numpy.sin(delta * t)
        s_t_normalized = s_t / 2.0
        signal = (s_t_normalized * amplitude).astype(numpy.int16)

        sound_buffer = Tone._create_buffer(signal, speaker)

        if filename:
            Tone.save_wav(sound_buffer, filename)
        else:
            sound = pygame.sndarray.make_sound(sound_buffer)
            sound.play(loops=0, maxtime=int(duration * 1000))
            time.sleep(duration)

    @staticmethod
    def get_sound_segment_signal(alpha, beta, gamma, delta, duration=1):
        """
        Calculates and returns the raw signal array for formula (3).
        """
        num_sample = int(round(duration * numpy.round(sample_rate)))
        amplitude = 2 ** (bits - 1) - 1
        t = numpy.linspace(0, duration, num_sample, endpoint=False)
        
        def g(x):
            return (numpy.mod(x, 2 * numpy.pi) < numpy.pi).astype(numpy.float32)
        
        s_t = g(alpha * t) * numpy.sin(gamma * t) + g(beta * t) * numpy.sin(delta * t)
        s_t_normalized = s_t / 2.0
        return (s_t_normalized * amplitude).astype(numpy.int16)

