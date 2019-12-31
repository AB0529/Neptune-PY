# Creates the video object
class Setup_Video:
    def __init__(self, v, requestor):
        self.url = v['video']['url'] # Video url
        self.title = v['video']['title'] # Video title
        self.thumbnail = v['thumbnail']['default']['url'] # Video thumbnail url
        self.requested_by = requestor # Song requestor
    