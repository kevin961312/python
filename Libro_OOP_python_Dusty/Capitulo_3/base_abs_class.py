import abc

class MediaLoader(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshock__(cls,c):
        if cls is MediaLoader:
            attrs = set(dir(c))
            if set(cls.__abstractmethods__) <= atrrs:
                return True
        return NotImplemented
#error
#class Wav(MediaLoader):
#    pass
#x=Wav

class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        print("Play")

song = Ogg()
song.play()