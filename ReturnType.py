class ReturnType:
    _MULTIPLE_CHOICE = "MultiChoice"
    _DISPLAY_DATA = "DisplayData"
    _AUDIO_MEDIA = "AudioMedia"
    _VIDEO_MEDIA = "VideoMedia"

    @staticmethod
    def _format_return(return_type, payload): return {"Type": return_type, "Payload": payload}

    @classmethod
    def multi_choice(cls, content_title: str, content: str, choice1: str, choice2: str, source: str):
        return cls._format_return(
            return_type=cls._MULTIPLE_CHOICE,
            payload={
                "Title": content_title,
                "Content": content,
                "Choice1": choice1,
                "Choice2": choice2,
                "Source": source,
            }
        )

    @classmethod
    def display_data(cls, content_title: str, content: str, source: str):
        return cls._format_return(
            return_type=cls._DISPLAY_DATA,
            payload={
                "Title": content_title,
                "Content": content,
                "Source": source
            }
        )

    @classmethod
    def audio_media(cls, content_title: str, stream_url: str, source: str):
        return cls._format_return(
            return_type=cls._AUDIO_MEDIA,
            payload={
                "Title": content_title,
                "StreamUrl": stream_url,
                "Source": source
            }
        )

    @classmethod
    def video_media(cls, content_title: str, stream_url: str, source: str):
        return cls._format_return(
            return_type=cls._VIDEO_MEDIA,
            payload={
                "Title": content_title,
                "StreamUrl": stream_url,
                "Source": source
            }
        )