from youtubesearchpython import VideosSearch
import youtube_dl, os, subprocess


def run():
    ydl = youtube_dl.YoutubeDL()
    search_query = input("(search) > ")
    while( search_query != 'q'):
        if len(search_query) == 0:
            print("No search query provided.")
        print("Searching", search_query)
        try:
            videosSearch = VideosSearch(search_query, limit = 10)
            results = videosSearch.result()['result']
            for i,j in enumerate(results):
                print(i, j['title'])
            selected_video_num = int(input("(select) > "))
            result = results[selected_video_num]
            info_dict = ydl.extract_info(result['id'], download=False)
            url = info_dict['formats'][0]['url']
            print('Playing', result['title'])
            with open(os.devnull, "w") as devnull:
                subprocess.run(['vlc', url, '--play-and-exit', '--meta-title=%s' % result['title']], shell=False, stderr=devnull)
            #os.system('/usr/bin/vlc "%s" --meta-title="%s"' % (url, result['title']))
        except Exception as ex:
            print(ex)
        search_query = input("(search) > ")

if __name__ == '__main__':
    run()
