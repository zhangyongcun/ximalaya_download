import aria2p
import requests

headers = {'Content-Type': 'application/json', 'User-Agent': 'PostmanRuntime/7.13.0', 'Accept': '*/*',
           'Cache-Control': 'no-cache', 'host': 'www.ximalaya.com:443', 'Connection': 'close'}

album_id = str(335347)
base_url = "http://www.ximalaya.com/revision/play/album?albumId=" + album_id + "&sort=0&pageSize=30&pageNum="
base_download_path = '~/Downloads/xmly/'

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)


def get_tracks(request_url, page_num):
    resp = requests.get(url=request_url, headers=headers)
    data = resp.json()
    if data['ret'] == 200:
        tracks = data['data']['tracksAudioPlay']
        for track in tracks:
            track_name = track['trackName'] + '.m4a'
            src = track['src']
            down_file(src, base_download_path, track_name)
        if data['data']['hasMore']:
            get_page_data(page_num + 1)


def down_file(src, download_path, file_name):
    aria2.add_uris(uris=[src, ], options={'dir': download_path, 'out': file_name})


def get_page_data(page_num):
    request_url = base_url + str(page_num)
    get_tracks(request_url, page_num)


if __name__ == '__main__':
    get_page_data(1)
    print('创建下载任务成功')

