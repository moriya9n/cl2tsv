# cl2tsv
common log format to tsv

timestamp is converted to iso format

```
cl2tsv.py
```

convert stdin

```
cl2tsv.py filename...
```

filename can be plain file or .gz file.
files with .gz extension are unzipped internally then converted.

## docker

docker image

```
docker run -i --rm moriya9n/cl2tsv
```

example (how to observe 404 accessed by googlebot)

```
zcat  -f $(ls -tr /var/log/nginx/access.log*) | docker run -i --rm moriya9n/cl2tsv | grep -i googlebot | cut -f 4,5,6 | grep 404
```

## related article

[common log format to tsv](https://kizamiudn.xyz/linux/common-log-format-to-tsv/)
