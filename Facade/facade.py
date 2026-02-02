# Subsystem Classes
class Amplifier:
    def on(self):
        print("Amplifier on")

    def off(self):
        print("Amplifier off")

    def set_volume(self, level):
        print(f"Amplifier setting volume to {level}")

class Tuner:
    def on(self):
        print("Tuner on")

    def off(self):
        print("Tuner off")

class DvdPlayer:
    def on(self):
        print("DVD Player on")

    def off(self):
        print("DVD Player off")

    def play(self, movie):
        print(f"DVD Player playing '{movie}'")

    def stop(self):
        print("DVD Player stopped")

class Projector:
    def on(self):
        print("Projector on")
    
    def off(self):
        print("Projector off")

    def wide_screen_mode(self):
        print("Projector in widescreen mode (16x9 aspect ratio)")

class TheaterLights:
    def dim(self, level):
        print(f"Theater Ceiling Lights dimming to {level}%")

    def on(self):
        print("Theater Ceiling Lights on")

class Screen:
    def down(self):
        print("Theater Screen going down")

    def up(self):
        print("Theater Screen going up")

class PopcornPopper:
    def on(self):
        print("Popcorn Popper on")

    def pop(self):
        print("Popcorn Popper popping popcorn!")

    def off(self):
        print("Popcorn Popper off")

# Facade Class
class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, projector, lights, screen, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("\nShutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.off()
