import librosa
import librosa.display
import moviepy.editor as mpy
from tqdm import tqdm

# define input and output files
video_file = 'test.mp4'
audio_file = 'audio.wav'

# extract audio from video file
video_clip = mpy.VideoFileClip(video_file)
video_clip.fps = 25
audio_clip = video_clip.audio
audio_clip.write_audiofile(audio_file)

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
video_clip = mpy.VideoFileClip(video_file)

# calculate length of audio in seconds
audio_length = librosa.get_duration(y=y, sr=sr)

# create clips from animation and video clip
animation_clip = animation.set_duration(audio_length)
video_clip = video_clip.subclip(0, audio_length)

# concatenate clips and write to file
final_clip = mpy.concatenate_videoclips([animation_clip, video_clip])
final_clip.write_videofile('final.mp4', fps=30, progress_bar=True)
