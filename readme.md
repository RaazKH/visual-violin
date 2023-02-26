# Visual Violin

Visual Violin is a Python script that creates a video file with a spectrogram animation overlaid on top of a given video file. The script extracts the audio from the video file, creates a mel spectrogram from the audio, and then animates the spectrogram. The resulting animation is overlaid on top of the video file to create a new video with the spectrogram visualization.

## Requirements

- Python 3.6 or higher
- moviepy
- librosa
- matplotlib
- numpy

## Usage

To use Visual Violin, follow these steps:

1. Install the required packages by running `pip3 install moviepy librosa matplotlib numpy`.
2. Place your input video file in the same directory as the `visual_violin.py` script.
3. Run the script by executing `python3 visual_violin.py`. The resulting video file will be saved as `output.mp4` in the same directory.

You can modify the input video file name and output video file name by editing the `video_file` and `output_file` variables in the script.

## Notes

- The script assumes that the input video file has an audio track.
- The output video file will have the same length as the audio track in the input video file.
- The script may take several minutes to run, depending on the length of the video and the performance of your computer.
