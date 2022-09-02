from Backend.ReturnTypes.BaseClasses import ReturnTypeBase


class DisplayData(ReturnTypeBase):
    def __init__(self, content_title: str, content_text: str, source_name: str, source_url: str):
        super(DisplayData, self).__init__()

        self.content_title = content_title
        self.content_text = content_text
        self.source = self.format_source(source_name, source_url)


class AudioMediaData(ReturnTypeBase):
    def __init__(self, content_title: str, stream_url: str, source_name: str, source_url: str):
        super(AudioMediaData, self).__init__()

        self.content_title = content_title
        self.stream_url = stream_url
        self.source = self.format_source(source_name, source_url)


class VideoMediaData(ReturnTypeBase):
    def __init__(self, content_title: str, stream_url: str, source_name: str, source_url: str):
        super(VideoMediaData, self).__init__()

        self.content_title = content_title
        self.stream_url = stream_url
        self.source = self.format_source(source_name, source_url)


class MultipleChoiceData(ReturnTypeBase):
    def __init__(self, content_title: str, content_text: str,
                 choice1: str, choice2: str, source_name: str, source_url: str):
        super(MultipleChoiceData, self).__init__()

        self.content_title = content_title
        self.content_text = content_text
        self.choice1 = choice1
        self.choice2 = choice2
        self.source = self.format_source(source_name, source_url)


class TestTypeData(ReturnTypeBase):
    """THIS DATA RETURN TYPE IS TO BE USED ONLY FOR TESTING DURING DEVELOPMENT."""

    def __init__(self, text):
        super(TestTypeData, self).__init__()

        self.text = text
        self.data = self.__doc__
