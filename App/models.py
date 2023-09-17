
class Clip(object):

    title: str
    link: str
    clipper: str
    clip_length: int

    def __len__(self) -> int:
        return self.clip_length