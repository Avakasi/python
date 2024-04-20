class Television:


    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializization of the Television"""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        

    def power(self) -> None:
        """Power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute status of the television."""
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted == True:
                self.__save_volume = self.__volume  
                self.__volume = Television.MIN_VOLUME 
            else:
                self.__volume = self.__save_volume 



    def channel_up(self) -> None:
        """Increase the channel of the television."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel of the television."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase the volume of the television."""
        if self.__status:
            self.__muted = False
            self.__volume = self.__save_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume of the television."""
        if self.__status:
            self.__muted = False
            self.__volume = self.__save_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1




    def __str__(self) -> str:
        """Return string representation of the Television object."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
