from pathlib import Path
import os
import re

import librosa
import soundfile as sf

def getMusicLis():
    directory = r"F:\BaiduNetdiskDownload\mp3 320k"

    def list_files(directory, pattern=None):
        path = Path(directory)
        for file in path.rglob('*'):
            if file.is_file() and (not pattern or pattern.match(str(file))):
                yield file

    pattern = re.compile(r'.*\.mp3$')
    for file in list_files(directory, pattern):
        print(file, ",")


def to180bpm(music_file):
    r = open(music_file)

    for line in r:
        t = line.split(',')
        music, bpm = t[0].strip(), int(t[1])
        a, b = 180 / bpm, 180 / (2 * bpm)
        times = b if abs(1 - a) > abs(1 - b) else a
        save_file = "./out/180_" + os.path.basename(music)
        print(f"{save_file} {bpm} convert to {times}")
        try:
            y, sr = sf.read(music)
            print(y.shape, sr)
            # y, sr = librosa.audioread(music, sr=None) # 出错
            y_change = librosa.effects.time_stretch(y.T, rate=times)
            print(y_change.shape);
            sf.write(save_file, y_change.T, sr)
        except Exception as e:
            print(f"{save_file} 发生异常 {e}")
            raise e

music_file = r"todo.csv"

# getMusicLis()

to180bpm(music_file)