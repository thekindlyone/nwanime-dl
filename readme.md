# nwanime-dl Anime Downloader   
## Downloads anime from http://www.nwanime.com/                             
[![Supported Python versions](https://pypip.in/py_versions/nwanime_dl/badge.svg)](https://pypi.python.org/pypi/<nwanime_dl>/)
[![License](https://pypip.in/license/nwanime_dl/badge.svg)](https://pypi.python.org/pypi/nwanime_dl/)
[![Development Status](https://pypip.in/status/nwanime_dl/badge.svg)](https://pypi.python.org/pypi/nwanime_dl/)

###Note: Currently works only for linux as it uses wget for the final download.


###Installation:
git clone this repo. then run       
```python setup.py install```          
or               
```pip install nwanime-dl```


###Dependencies:
1. Requests library
2. Beautifulsoup library
3. wget

###Usage:       
```nwanime-dl <url>```       
```nwanime-dl -i 10 <url>```      


```
usage: nwanime-dl [-h] [-i ITERATIVE] [-d DIRECTORY] url

positional arguments:
  url                   url to download video from. In case of iterative
                        starting url

optional arguments:
  -h, --help            show this help message and exit
  -i ITERATIVE, --iterative ITERATIVE
                        For range downloads. eg. nwanime-dl -i 10 <url> will
                        download iteratively the video in <url> and the next 9
                        videos(total 10)
  -d DIRECTORY, --directory DIRECTORY
                        Explicitly specify output directory. Current directory
                        by default.

```

###Example:     
```
mac → nwanime-dl -i 5 http://www.nwanime.com/nanatsu-no-taizai-episode-3/video/640cffdd3031e7ff06ce/
Nanatsu no Taizai Episode 3
fetching mirrors
mirrors found
downloadable mirror found
attempting download from VidWoot
--2015-01-13 14:26:51--  http://stream.vidcache.net/5e608967206d65ff32d6a6fc9224b8cdcd7343a6.mp4?client_file_id=857520
Resolving stream.vidcache.net... 162.211.92.130, 162.211.92.140, 162.211.92.133, ...
Connecting to stream.vidcache.net|162.211.92.130|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: http://s31.vidcache.net/stream/5e608967206d65ff32d6a6fc9224b8cdcd7343a6?client_file_id=857520&redirected_from=s18.vidcache.net [following]
--2015-01-13 14:26:51--  http://s31.vidcache.net/stream/5e608967206d65ff32d6a6fc9224b8cdcd7343a6?client_file_id=857520&redirected_from=s18.vidcache.net
Resolving s31.vidcache.net... 162.211.92.143
Connecting to s31.vidcache.net|162.211.92.143|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 57028263 (54M) [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 3.mp4'

Nanatsu no Taizai Episode 3.mp4          99%[==============================================================================> ]  54.35M  1.74MB/s   in 2m 17s 

2015-01-13 14:29:12 (405 KB/s) - Connection closed at byte 56992560. Retrying.

--2015-01-13 14:29:13--  (try: 2)  http://s31.vidcache.net/stream/5e608967206d65ff32d6a6fc9224b8cdcd7343a6?client_file_id=857520&redirected_from=s18.vidcache.net
Connecting to s31.vidcache.net|162.211.92.143|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 57028263 (54M), 35703 (35K) remaining [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 3.mp4'

Nanatsu no Taizai Episode 3.mp4         100%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>]  54.39M   192KB/s   in 0.2s   

2015-01-13 14:29:14 (192 KB/s) - 'Nanatsu no Taizai Episode 3.mp4' saved [57028263/57028263]

Nanatsu no Taizai Episode 4
fetching mirrors
mirrors found
downloadable mirror found
attempting download from VidWoot
--2015-01-13 14:29:17--  http://stream.vidcache.net/98ac2fc8be2d6973385ccf0a6a67507231fffb72.mp4?client_file_id=859550
Resolving stream.vidcache.net... 162.211.92.143
Connecting to stream.vidcache.net|162.211.92.143|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: http://s29.vidcache.net/stream/98ac2fc8be2d6973385ccf0a6a67507231fffb72?client_file_id=859550&redirected_from=s31.vidcache.net [following]
--2015-01-13 14:29:18--  http://s29.vidcache.net/stream/98ac2fc8be2d6973385ccf0a6a67507231fffb72?client_file_id=859550&redirected_from=s31.vidcache.net
Resolving s29.vidcache.net... 162.211.92.141
Connecting to s29.vidcache.net|162.211.92.141|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 56155956 (54M) [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 4.mp4'

Nanatsu no Taizai Episode 4.mp4          99%[==============================================================================> ]  53.52M   258KB/s   in 2m 8s  

2015-01-13 14:31:27 (428 KB/s) - Connection closed at byte 56120254. Retrying.

--2015-01-13 14:31:28--  (try: 2)  http://s29.vidcache.net/stream/98ac2fc8be2d6973385ccf0a6a67507231fffb72?client_file_id=859550&redirected_from=s31.vidcache.net
Connecting to s29.vidcache.net|162.211.92.141|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 56155956 (54M), 35702 (35K) remaining [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 4.mp4'

Nanatsu no Taizai Episode 4.mp4         100%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>]  53.55M   192KB/s   in 0.2s   

2015-01-13 14:31:29 (192 KB/s) - 'Nanatsu no Taizai Episode 4.mp4' saved [56155956/56155956]

Nanatsu no Taizai Episode 5
fetching mirrors
mirrors found
downloadable mirror found
attempting download from VidWoot
--2015-01-13 14:31:32--  http://stream.vidcache.net/4980e74c38fca21a57a4ff2665d305b7cfc3887a.mp4?client_file_id=860866
Resolving stream.vidcache.net... 162.211.92.135, 162.211.92.143, 162.211.92.140, ...
Connecting to stream.vidcache.net|162.211.92.135|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: http://s16.vidcache.net/stream/4980e74c38fca21a57a4ff2665d305b7cfc3887a?client_file_id=860866&redirected_from=s23.vidcache.net [following]
--2015-01-13 14:31:32--  http://s16.vidcache.net/stream/4980e74c38fca21a57a4ff2665d305b7cfc3887a?client_file_id=860866&redirected_from=s23.vidcache.net
Resolving s16.vidcache.net... 162.211.92.152
Connecting to s16.vidcache.net|162.211.92.152|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 58609845 (56M) [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 5.mp4'

Nanatsu no Taizai Episode 5.mp4          99%[==============================================================================> ]  55.86M   257KB/s   in 1m 55s 

2015-01-13 14:33:28 (495 KB/s) - Connection closed at byte 58574079. Retrying.

--2015-01-13 14:33:29--  (try: 2)  http://s16.vidcache.net/stream/4980e74c38fca21a57a4ff2665d305b7cfc3887a?client_file_id=860866&redirected_from=s23.vidcache.net
Connecting to s16.vidcache.net|162.211.92.152|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 58609845 (56M), 35766 (35K) remaining [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 5.mp4'

Nanatsu no Taizai Episode 5.mp4         100%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>]  55.89M  --.-KB/s   in 0.1s   

2015-01-13 14:33:29 (366 KB/s) - 'Nanatsu no Taizai Episode 5.mp4' saved [58609845/58609845]

Nanatsu no Taizai Episode 6
fetching mirrors
mirrors found
downloadable mirror found
attempting download from VidWoot
--2015-01-13 14:33:33--  http://stream.vidcache.net/107127e7055fbbcc522be87e2a7c5c58f018642e.mp4?client_file_id=862402
Resolving stream.vidcache.net... 162.211.92.144, 162.211.92.132, 162.211.92.140, ...
Connecting to stream.vidcache.net|162.211.92.144|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: http://s16.vidcache.net/stream/107127e7055fbbcc522be87e2a7c5c58f018642e?client_file_id=862402&redirected_from=s32.vidcache.net [following]
--2015-01-13 14:33:34--  http://s16.vidcache.net/stream/107127e7055fbbcc522be87e2a7c5c58f018642e?client_file_id=862402&redirected_from=s32.vidcache.net
Resolving s16.vidcache.net... 162.211.92.152
Connecting to s16.vidcache.net|162.211.92.152|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 56482475 (54M) [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 6.mp4'

Nanatsu no Taizai Episode 6.mp4          99%[==============================================================================> ]  53.83M   253KB/s   in 1m 50s 

2015-01-13 14:35:25 (501 KB/s) - Connection closed at byte 56446772. Retrying.

--2015-01-13 14:35:26--  (try: 2)  http://s16.vidcache.net/stream/107127e7055fbbcc522be87e2a7c5c58f018642e?client_file_id=862402&redirected_from=s32.vidcache.net
Connecting to s16.vidcache.net|162.211.92.152|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 56482475 (54M), 35703 (35K) remaining [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 6.mp4'

Nanatsu no Taizai Episode 6.mp4         100%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>]  53.87M   180KB/s   in 0.2s   

2015-01-13 14:35:26 (180 KB/s) - 'Nanatsu no Taizai Episode 6.mp4' saved [56482475/56482475]

Nanatsu no Taizai Episode 7
fetching mirrors
mirrors found
downloadable mirror found
attempting download from VidWoot
--2015-01-13 14:35:29--  http://stream.vidcache.net/baba6033aa721f77e4617ee21c71a58d3f2f46c5.mp4?client_file_id=865266
Resolving stream.vidcache.net... 162.211.92.130, 162.211.92.141, 162.211.92.132, ...
Connecting to stream.vidcache.net|162.211.92.130|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 55989282 (53M) [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 7.mp4'

Nanatsu no Taizai Episode 7.mp4          99%[==============================================================================> ]  53.36M   221KB/s   in 2m 8s  

2015-01-13 14:37:39 (428 KB/s) - Connection closed at byte 55953581. Retrying.

--2015-01-13 14:37:40--  (try: 2)  http://stream.vidcache.net/baba6033aa721f77e4617ee21c71a58d3f2f46c5.mp4?client_file_id=865266
Connecting to stream.vidcache.net|162.211.92.130|:80... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 55989282 (53M), 35701 (35K) remaining [video/mp4]
Saving to: 'Nanatsu no Taizai Episode 7.mp4'

Nanatsu no Taizai Episode 7.mp4         100%[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>]  53.40M   178KB/s   in 0.2s   

2015-01-13 14:37:43 (178 KB/s) - 'Nanatsu no Taizai Episode 7.mp4' saved [55989282/55989282]


******************************
Nanatsu no Taizai Episode 3	Done
Nanatsu no Taizai Episode 4	Done
Nanatsu no Taizai Episode 5	Done
Nanatsu no Taizai Episode 6	Done
Nanatsu no Taizai Episode 7	Done
******************************
mac → 
```


### to do:              
1. setuptools compatibility   [X]
2. setuptools command line script   [X]
3. range downloader    [X]
4. reports on undownloadable episodes and undiscovered mirrors
5. windows and python 3 support
6. -D option for explicitly specifying output directory    [X]


special thanks to [Derrick Kearney](https://github.com/diek) for helping me test it .