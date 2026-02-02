# Subsystem classes
class DVDPlayer:
    def on(self):
        print("DVD Player is ON")
    def play(self, movie):
        print(f"Playing movie: {movie}")
    def off(self):
        print("DVD Player is OFF")

class Projector:
    def on(self):
        print("Projector is ON")
    def wide_screen_mode(self):
        print("Projector in widescreen mode")
    def off(self):
        print("Projector is OFF")

class SoundSystem:
    def on(self):
        print("Sound System is ON")
    def set_volume(self, level):
        print(f"Volume set to {level}")
    def off(self):
        print("Sound System is OFF")

# Facade class
class HomeTheaterFacade:
    def __init__(self, dvd, projector, sound):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound.on()
        self.sound.set_volume(10)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd.off()
        self.sound.off()
        self.projector.off()

# Client code
if __name__ == "__main__":
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()

    home_theater = HomeTheaterFacade(dvd, projector, sound)
    home_theater.watch_movie("Inception")
    home_theater.end_movie()
