def run():
    from youtubesearchpython import VideosSearch
    import youtube_dl, os, sys
    search_query = ' '.join(sys.argv[1:]).strip()
    if len(search_query) == 0:
        print("No search query provided.")
        exit()
    ydl = youtube_dl.YoutubeDL()
    print("Searching", search_query)
    videosSearch = VideosSearch(search_query, limit = 1)
    result = videosSearch.result()['result'][0]
    info_dict = ydl.extract_info(result['id'], download=False)
    url = info_dict['formats'][0]['url']
    os.system('/usr/bin/vlc "%s"' % url)
