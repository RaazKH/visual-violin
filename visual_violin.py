import librosa
import librosa.display
import numpy as np
import cv2
from tqdm import tqdm

# Load audio file
y, sr = librosa.load('test.wav', sr=44100)

# Create mel spectrogram
with tqdm(total=100, desc='Creating spectrogram') as pbar:
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, hop_length=512)
    pbar.update(20)

    # Convert to log scale (dB). Use the peak power (max) as reference.
    S_dB = librosa.power_to_db(S, ref=np.max)
    pbar.update(20)

    # Rescale the amplitude range to between 0 and 255
    spectrogram = cv2.normalize(S_dB, None, 0, 255, cv2.NORM_MINMAX)
    pbar.update(20)

    # Convert to uint8 format for saving as an image
    spectrogram = spectrogram.astype('uint8')
    pbar.update(20)

    # Save the spectrogram as an image file
    cv2.imwrite('spectrogram.png', spectrogram)
    pbar.update(20)
