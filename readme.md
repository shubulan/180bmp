# Create a playlist of 180-step songs in bulk using the Librosa library

## enviroment
1. [use miniconda in vscode](https://code.visualstudio.com/docs/python/environments)
2. [Use the Tsinghua mirror/source.](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
3. install librosa

```
conda install -c conda-forge librosa  
```

## change music to 180 bpm
There are two function in 180bpm.py

1. `getMusicLis`: walk given directory to get all music files and print them. You can copy the output and save it into a `*.csv` file.

You need to complete bpm of all the music. You can use two means to get bpm of a music:
* [search on internet](https://getsongbpm.com/)
* [do it by hand](https://www.beatsperminuteonline.com/zh/home/index/tap-bpm)
* ... discover your way...

finally you get a `*.csv` file like this
```
a.flac, 120
b.flac, 96
c.flac, 130
```
There is a example in [todo.csv](todo.csv)

2. `to180bpm`: read the csv file line by line, convert the music to 180bpm and save it into `./out` directory
