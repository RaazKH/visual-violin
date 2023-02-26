# Visual Violin

Visual Violin is a Python script that creates a mel spectrogram from an audio file and saves it as an image file. This can be useful for visualizing the frequency content of audio recordings, such as violin performances.

## Installation

1. Install the required libraries using pip:

    ```
    pip install librosa opencv-python
    ```

2. Place your audio file in the same directory as the `visual_violin.py` script.

## Usage

1. Run the `visual_violin.py` script using Python:

    ```
    python visual_violin.py
    ```

2. The script will create a mel spectrogram from the audio file and save it as `spectrogram.png` in the same directory.

## Customization

You can customize the parameters of the mel spectrogram by editing the `librosa.feature.melspectrogram` function in the `visual_violin.py` script. For example, you can adjust the number of mel frequency bands (`n_mels`), the frequency range (`fmin` and `fmax`), and the hop length (`hop_length`). You can also adjust the size and format of the output image by editing the `figsize` and `dpi` parameters in the `cv2.imwrite` function.

## Dependencies

Visual Violin requires the following Python libraries:

- librosa
- opencv-python

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
