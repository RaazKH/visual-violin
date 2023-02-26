import librosa
import librosa.display
import moviepy.editor as mpy
import numpy as np
from tqdm import tqdm

# define input and output files
audio_file = 'test.wav'

# load audio file
y, sr = librosa.load(audio_file)

# create mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

# convert to dB
S_dB = librosa.power_to_db(S, ref=np.max)

# create figure
fig, ax = plt.subplots(figsize=(12, 8))

# display spectrogram on axis
img = librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, ax=ax)

# create animation
animation = mpy.ImageSequenceClip([ax.get_figure().canvas.renderer.buffer_rgba()], fps=30)

# create video clip
audio_clip = mpy.AudioFileClip(audio_file)
audio_length = audio_clip.duration
video_clip = mpy.VideoClip(lambda x: x, duration=audio_length)

# create clips from animation and video clip
animation_clip = animation.set_duration(audio_length)

# concatenate clips and write to file
final_clip = mpy.CompositeVideoClip([animation_clip.set_position((0,0)), video_clip.set_position((0,0))])
final_clip = final_clip.set_audio(audio_clip)
final_clip.write_videofile('final.mp4', fps=30, progress_bar=True)
