nwanime-dl Anime Downloader
===========================

Downloads anime from http://www.nwanime.com/
--------------------------------------------



Note: Currently works only for linux and mac as it uses wget for the final download.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installation:
~~~~~~~~~~~~~

| git clone this repo. then run
| ``python setup.py install``
| or
| ``pip install nwanime_dl``

Dependencies:
~~~~~~~~~~~~~

1. Requests library
2. Beautifulsoup library
3. wget

Usage:
~~~~~~

| ``nwanime-dl <url>``
| ``nwanime-dl -i 10 <url>``

::

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

Example:
~~~~~~~~

::

    $ nwanime-dl -i 10 http://www.nwanime.com/nanatsu-no-taizai-episode-8/video/a791265c48f25acd0c33/
    Nanatsu no Taizai Episode 8
    fetching mirrors
    mirrors found
    downloadable mirror found
    attempting download from VidWoot
    --2015-01-14 09:08:56--  http://stream.vidcache.net/bd472ce9e372e6ece2a31f1b499231ad27b492e1.mp4?client_file_id=868256
    Resolving stream.vidcache.net (stream.vidcache.net)... 162.211.92.135, 162.211.92.144, 162.211.92.132, ...
    Connecting to stream.vidcache.net (stream.vidcache.net)|162.211.92.135|:80... connected.
    HTTP request sent, awaiting response... 302 Moved Temporarily
    Location: http://s17.vidcache.net/stream/bd472ce9e372e6ece2a31f1b499231ad27b492e1?client_file_id=868256&redirected_from=s23.vidcache.net [following]
    --2015-01-14 09:08:57--  http://s17.vidcache.net/stream/bd472ce9e372e6ece2a31f1b499231ad27b492e1?client_file_id=868256&redirected_from=s23.vidcache.net
    Resolving s17.vidcache.net (s17.vidcache.net)... 199.87.232.131
    Connecting to s17.vidcache.net (s17.vidcache.net)|199.87.232.131|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 57291492 (55M) [video/mp4]
    Saving to: ‘Nanatsu no Taizai Episode 8.mp4’

    99% [==========================================> ] 5,72,55,778 71.2KB/s   in 13m 6s 

    .......
    .......
    .......

    2015-01-14 16:57:08 (14.5 KB/s) - Connection closed at byte 29901248. Retrying.

    --2015-01-14 16:57:10--  (try: 3)  http://s29.vidcache.net/stream/6145b72c88ffcfd8ed763b450fe9e6667c2b43db?client_file_id=903136&redirected_from=s23.vidcache.net
    Connecting to s29.vidcache.net (s29.vidcache.net)|162.211.92.141|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: unspecified [text/xml]
    Saving to: ‘Nanatsu no Taizai Episode 13.mp4’

        [ <=>                                        ] 4,436       --.-K/s   in 0s      

    2015-01-14 16:57:18 (9.92 MB/s) - ‘Nanatsu no Taizai Episode 13.mp4’ saved [29901248]


    ******************************
    Nanatsu no Taizai Episode 8 Done
    Nanatsu no Taizai Episode 9 Done
    Nanatsu no Taizai Episode 10    Done
    Nanatsu no Taizai Episode 11    Done
    Nanatsu no Taizai Episode 12    Done
    Nanatsu no Taizai Episode 13    Done
    ******************************

to do:
~~~~~~

1. setuptools compatibility [X]
2. setuptools command line script [X]
3. range downloader [X]
4. reports on undownloadable episodes and undiscovered mirrors
5. windows and python 3 support
6. -D option for explicitly specifying output directory [X]

special thanks to `Derrick Kearney <https://github.com/diek>`_ for
helping me test it .


