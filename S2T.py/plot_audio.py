import wave
import numpy as np
import matplotlib.pyplot as plt


obj = wave.open(r"C:\Users\MY LAPTOP\Downloads\TestRecording.wav","rb" )

# print(obj.getnchannels())
frame_freq=obj.getframerate()
# print(frame_freq)
n_frame=obj.getnframes()   #number of samples
print(n_frame)
signal_wave=obj.readframes(-1)    #actual signal

obj.close()

t_audio=n_frame/frame_freq   #time of audio

# print(n_frame)
# print(t_audio)

signal_array= np.frombuffer(signal_wave,dtype=np.int16)
print(len(signal_array))

# for stereo:
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times=np.linspace(0,t_audio,n_frame) 

#plot the audio
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Audio')
plt.ylabel('Signal Value l_channel')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

plt.figure(figsize=(15, 5))
plt.plot(times, r_channel)
plt.title('Audio')
plt.ylabel('Signal Value r_channel')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


#plot the frequncy
plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=frame_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()