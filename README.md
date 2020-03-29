## ass2srt

A tool that convert .ass subtitles to .srt

### Install
```
pip install ass2srt
```

### Usage
```
$ ass2srt -h

usage: ass2srt.py [-h] [-s {zh,en,fr,de}] [-l {0,1,2}] [-i] file

positional arguments:
  file                  .ass file to convert

optional arguments:
  -h, --help            show this help message and exit
  -s {zh,en,fr,de}, --suffix {zh,en,fr,de}
                        add suffix to subtitles name
  -l {0,1,2}, --line {0,1,2}
                        keep double subtitles
  -i, --info            display subtitles infomation
  -o OUT, --out OUT     output file name

```

### Example :
```
ass2srt Movies.S01.E01.Name.ass
```

### Used as a Library

You can use asstosrt on your program easily.
```
import ass2srt
subtitles=ass2srt.Ass2srt("Movies.S01E01.Name.ass")
subtitles.to_srt()
```

### License

MIT License

### Bugs and Issues

Please visit [GitHub](https://github.com/zcq100/ass2srt).
