from pytube import YouTube

from ReturnType import ReturnType


class GetYoutubeVideo:
    """This Function Takes A Video's Url And Returns The Stream Url"""

    class_type = "Online"

    def __call__(self, video_url):
        yt = YouTube(video_url)
        stream_urls = yt.streams.filter(progressive=True, file_extension="mp4")
        stream_url_480p = stream_urls.filter(res="480p")
        if stream_url_480p:
            stream_url_480p = stream_url_480p[0]
            return ReturnType.video_media(content_title=stream_url_480p.title, stream_url=stream_url_480p.url,
                                          source="Youtube")
        else:
            stream_url_720p = stream_urls.filter(res="720p")[0]
            return ReturnType.video_media(content_title=stream_url_720p.title, stream_url=stream_url_720p.url,
                                          source="Youtube")


print(GetYoutubeVideo()("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
