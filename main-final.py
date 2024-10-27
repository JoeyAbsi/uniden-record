import os
import wave
from datetime import datetime


def get_wav_files(folder_path):
    # Get all .wav files in the folder
    wav_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith('.wav')
    ]
    # Sort by last modified time
    wav_files.sort(key=lambda x: os.path.getmtime(x))
    return wav_files


def concatenate_wav_files(wav_files, output_file):
    # Open the first file to get parameters
    with wave.open(wav_files[0], 'rb') as wf:
        params = wf.getparams()

    # Create the output file with same parameters
    with wave.open(output_file, 'wb') as output_wav:
        output_wav.setparams(params)

        # Read and write data for each file
        for file_path in wav_files:
            with wave.open(file_path, 'rb') as wf:
                output_wav.writeframes(wf.readframes(wf.getnframes()))


if __name__ == '__main__':
    folder_path = input('Enter folder: ')
    output_file = folder_path + '-output.wav'           # Output file name
    f = open("log.txt", "w")

    wav_files = get_wav_files(folder_path)
    if not wav_files:
        f.write("No .wav files found in " + folder_path)
        f.close()
    else:
        concatenate_wav_files(wav_files, output_file)
        f.write(f"Successfully concatenated {len(wav_files)} .wav files into {output_file}.")
        f.close()
