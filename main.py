def run():
    from youtubesearchpython import VideosSearch
    import youtube_dl, os, sys

    ydl = youtube_dl.YoutubeDL()
    videosSearch = VideosSearch(' '.join(sys.argv[1:]), limit = 1)
    result = videosSearch.result()['result'][0]
    info_dict = ydl.extract_info(result['id'], download=False)
    url = info_dict['formats'][0]['url']
    os.system('/usr/bin/vlc "%s"' % url)
