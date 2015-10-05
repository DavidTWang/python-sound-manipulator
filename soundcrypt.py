import wave
import pyaudio

filename = "test.wav"
wf = wave.open(filename, 'rb')

pya = pyaudio.PyAudio()
stream = pya.open(format=pya.get_format_from_width(wf.getsampwidth()),
                  channels=wf.getnchannels(),
                  rate=wf.getframerate(),
                  output=True)

full_data = []
data = wf.readframes(1024)

while data:
    full_data.append(data)
    data = wf.readframes(1024)

data = ''.join(full_data)[::-1]

for i in range(0, len(data), 1024):
    stream.write(data[i:i+1024])
