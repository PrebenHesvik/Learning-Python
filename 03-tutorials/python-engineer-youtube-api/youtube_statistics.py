import requests
import json
from tqdm import tqdm


class YTstats:
    def __init__(self, api_key, channel_id):
        self.base_url = 'https://youtube.googleapis.com/youtube/v3/'
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):

        url = f'{self.base_url}channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0]['statistics']
        except:
            data = None
        self.channel_statistics = data
        return data

    def get_channel_video_data(self):
        # Get video ids
        channel_videos = self._get_channel_videos(limit=50)
        # Get video statistics
        parts = ['snippet', 'statistics', 'contentDetails']
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)
        self.video_data = channel_videos
        return self.video_data

    def _get_single_video_data(self, video_id, part):
        url = f'{self.base_url}videos?part={part}&id={video_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except:
            print('error')
            data = {}
        return data

    def _get_channel_videos(self, limit=None):
        url = f'{self.base_url}search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit, int):
            url += f'&maxResults={limit}'
        vid, npt = self._get_channel_videos_per_page(url)
        idx = 0
        while (npt is not None and idx < 10):
            nexturl = url + f'&pageToken={npt}'
            next_vid, npt = self._get_channel_videos_per_page(nexturl)
            vid.update(next_vid)
            idx += 1
        return vid

    def _get_channel_videos_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = {}
        if 'items' not in data:
            return channel_videos, None

        item_data = data['items']
        nextPageToken = data.get('nextPageToken', None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print('error')

        return channel_videos, nextPageToken

    def dump(self):
        if self.channel_statistics is not None and self.video_data is not None:

            fused_data = {
                self.channel_id: {
                    'channel_statistics': self.channel_statistics,
                    'video_data': self.video_data
                }
            }

            channel_title = self.video_data.popitem()[1].get(
                'channelTitle', self.channel_id)
            channel_title = channel_title.replace(' ', '_').lower()
            file_name = channel_title + '.json'
            with open(file_name, 'w') as f:
                json.dump(fused_data, f, indent=4)
