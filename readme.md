# nwanime-dl Anime Downloader   
## Downloads anime from http://www.nwanime.com/ 

usage:       
```python nwanime-dl <url>```

example:     
```
thekindlyone@deepthought:~/projects/nwanime-dl/nwanime-dl$ python nwanime-dl.py http://www.nwanime.com/sengoku-musou-tv-episode-1/video/6a32205a3d414589b48c/
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