from celery import shared_task
# from django.contrib.sites import requests
import requests
from models import VideoList

@shared_task()
def fetch_videos():
    API_KEY = "test"
    query = "test"

    params = {
        'key': API_KEY,
        'part': 'snippet',
        'type': 'video',
        'order': 'date',
        'maxResults': 10,
        'q': query
    }

    response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    data = response.json()
    for item in data.get('items', []):
        video = VideoList.objects.create(
            video_title=item['snippet']['title'],
            description=item['snippet']['description'],
            publishing_datetime=item['snippet']['publishedAt'],
            thumbnails_URLs=item['snippet']['thumbnails']['default']['url']
        )



