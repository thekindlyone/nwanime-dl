# nwanime-dl Anime Downloader   
## Downloads anime from http://www.nwanime.com/ 

###Installation:
git clone this repo. then run       
```python setup.py install```

###usage:       
```nwanime-dl <url>```       
```nwanime-dl -i 10 <url>```      
```
usage: nwanime-dl [-h] [-i ITERATIVE] url

positional arguments:
  url                   url to download video from. In case of iterative
                        starting url

optional arguments:
  -h, --help            show this help message and exit
  -i ITERATIVE, --iterative ITERATIVE
                        For range downloads. eg. nwanime-dl -i 10 <url> will
                        download iteratively the video in <url> and the next 9
                        videos(total 10)
```

###example:     
```
thekindlyone@deepthought:~/projects/nwanime-dl/nwanime-dl$ nwanime-dl http://www.nwanime.com/sengoku-musou-tv-episode-1/video/6a32205a3d414589b48c/
Sengoku Musou (TV) Episode 1
--2015-01-12 09:14:28--  http://stream.vidcache.net/b4f835b701c8196880142f5a5a9351790bd3c12b.mp4?client_file_id=902765
Resolving stream.vidcache.net (stream.vidcache.net)... 162.211.92.144, 162.211.92.130, 162.211.92.132, ...
Connecting to stream.vidcache.net (stream.vidcache.net)|162.211.92.144|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: http://s19.vidcache.net/stream/b4f835b701c8196880142f5a5a9351790bd3c12b?client_file_id=902765&redirected_from=s32.vidcache.net [following]
--2015-01-12 09:14:29--  http://s19.vidcache.net/stream/b4f835b701c8196880142f5a5a9351790bd3c12b?client_file_id=902765&redirected_from=s32.vidcache.net
Resolving s19.vidcache.net (s19.vidcache.net)... 162.211.92.131
Connecting to s19.vidcache.net (s19.vidcache.net)|162.211.92.131|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 58631106 (56M) [video/mp4]
Saving to: ‘Sengoku Musou (TV) Episode 1.mp4’

99% [=============================================================> ] 5,85,95,516 71.7KB/s   in 16m 54s

2015-01-12 09:31:27 (56.4 KB/s) - Connection closed at byte 58595516. Retrying.

--2015-01-12 09:31:28--  (try: 2)  http://s19.vidcache.net/stream/b4f835b701c8196880142f5a5a9351790bd3c12b?client_file_id=902765&redirected_from=s32.vidcache.net
Connecting to s19.vidcache.net (s19.vidcache.net)|162.211.92.131|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 58631106 (56M), 35590 (35K) remaining [video/mp4]
Saving to: ‘Sengoku Musou (TV) Episode 1.mp4’

100%[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>] 5,86,31,106 50.7KB/s   in 0.7s   

2015-01-12 09:31:32 (50.7 KB/s) - ‘Sengoku Musou (TV) Episode 1.mp4’ saved [58631106/58631106]

File Downloaded
```


### to do:              
1. setuptools compatibility   [X]
2. setuptools command line script   [X]
3. range downloader
4. reports on undownloadable episodes and undiscovered mirrors
5. windows and python 3 support