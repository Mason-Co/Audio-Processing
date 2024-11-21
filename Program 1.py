from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
import numpy as np
import wave

audio = AudioSegment.from_wav("VideoSound.wav")
obj = wave.open("VideoSound.wav", 'rb')
frames = obj.readframes(obj.getnframes())
obj.close()

audio2 = AudioSegment.from_wav("Roller.wav")
obj2 = wave.open("Roller.wav", 'rb')
frames2 = obj2.readframes(obj2.getnframes())

def plotAudio(file):
    plotter = wave.open(file, 'rb')
    sample_freq = plotter.getframerate()
    n_samples = plotter.getnframes()
    signal_wave = plotter.readframes(-1)
    plotter.close()
    t_audio = int(n_samples / sample_freq)

    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    times = np.linspace(0, t_audio, num=n_samples)

    plt.figure(figsize=(10,5))
    plt.plot(times, signal_array)
    plt.title("Audio Signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time (sec)")
    plt.xlim(0, t_audio)
    plt.show()

def clip(start, end):
    clipped_audio = audio2[start:end]
    clipped_audio.export("Edited.wav", format='wav')
    #play(clipped_audio)
    plotAudio("Edited.wav")

def multiTrack():
    tracks = audio2.overlay(audio)
    tracks.export("Edited.wav", format='wav')
    #play(tracks)
    plotAudio("Edited.wav")

def changeVolume(vol):
    volUp = AudioSegment.from_wav("Roller.wav")
    volUp += vol
    volUp.export("Edited.wav", format='wav')
    #play(volUp)
    plotAudio("Edited.wav")

def newFrameRate(frame_rate):

    rolled = wave.open("Edited.wav", 'wb')
    rolled.setnchannels(1)
    rolled.setsampwidth(2)
    rolled.setframerate(frame_rate)
    rolled.writeframes(frames2)
    #play(rolled)
    plotAudio("Edited.wav")

def getInfo():
    print("Number of Channels: ", obj2.getnchannels())
    print("Sample width: ", obj2.getsampwidth())
    print("Frame rate: ", obj2.getframerate())
    print("Number of frames: ", obj2.getnframes())
    print(f"Duration (Seconds): {audio2.duration_seconds:.2f}")
    plotAudio("Roller.wav")

def main():
    choice = int(input("What would you like to do?"
          "\n1-Clip"
          "\n2-Multiple Tracks"
          "\n3-Add Volume"
          "\n4-Change Frame Rate"
          "\n5-Get Information"))
    if choice == 1:
        print("Frames: ", obj2.getnframes())
        start = int(input("Input starting frame: "))
        end = int(input("Input end frame: "))
        clip(start, end)
    elif choice == 2:
        multiTrack()
    elif choice == 3:
        vol = int(input("Volume: "))
        changeVolume(vol)
    elif choice == 4:
        print("Frame rate: ", obj2.getframerate())
        frame_rate = int(input("New frame rate: "))
        newFrameRate(frame_rate)
    elif choice == 5:
        getInfo()


if __name__ == '__main__':
    main()
