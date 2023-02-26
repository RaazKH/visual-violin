import librosa
import librosa.display
import numpy as np
import cv2

# Load audio file
y, sr = librosa.load('test.wav', sr=44100)

# Create mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

# Convert to log scale (dB). Use the peak power (max) as reference.
S_dB = librosa.power_to_db(S, ref=np.max)

# Rescale the amplitude range to between 0 and 255
spectrogram = cv2.normalize(S_dB, None, 0, 255, cv2.NORM_MINMAX)

# Convert to uint8 format for saving as an image
spectrogram = spectrogram.astype('uint8')

# Save the spectrogram as an image file
cv2.imwrite('spectrogram.png', spectrogram)
