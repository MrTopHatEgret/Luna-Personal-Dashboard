from pytube import YouTube
from ReturnType import ReturnType


# Convert the function into a Function Class
def get_audio_url(audio_url: str):
    yt = YouTube(audio_url)
    stream_urls = yt.streams.filter(only_audio=True, file_extension="mp4")
    all_stream_abrs = [stream.abr for stream in stream_urls]
    all_stream_urls = [stream.url for stream in stream_urls]
    all_stream_titles = [stream.title for stream in stream_urls]

    max_abr_index = all_stream_abrs.index(max(all_stream_abrs))

    stream_url = all_stream_urls[max_abr_index]
    stream_url_title = all_stream_titles[max_abr_index]

    return ReturnType.audio_media(content_title=stream_url_title, stream_url=stream_url, source="Youtube")
