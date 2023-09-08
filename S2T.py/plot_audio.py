import wave
import numpy as np
import matplotlib.pyplot as plt


obj = wave.open(r"C:\Users\MY LAPTOP\Downloads\TestRecording.wav","rb" )

# print(obj.getnchannels())
sample_freq=obj.getframerate()
n_sample=obj.getnframes()   #number of samples
signal_wave=obj.readframes(-1)    #actual signal

obj.close()

t_audio=n_sample/sample_freq   #time of audio

print(n_sample)
# print(t_audio)

signal_array= np.frombuffer(signal_wave,dtype=np.int32)

# for stereo:
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times=np.linspace(0,t_audio,n_sample) 
l_channel_times = times[0::2]
r_channel_times = times[1::2]

#plot the audio
plt.figure(figsize=(15, 5))
plt.plot(l_channel_times, l_channel)
plt.title('Audio')
plt.ylabel('Signal Value l_channel')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

plt.figure(figsize=(15, 5))
plt.plot(r_channel_times, r_channel)
plt.title('Audio')
plt.ylabel('Signal Value r_channel')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


#plot the frequncy
plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()