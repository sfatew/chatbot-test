import pyaudio
import wave

CHUNK = 3200
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 44100

print(pyaudio.get_sample_size(pyaudio.paInt32))



