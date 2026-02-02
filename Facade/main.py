from facade import Amplifier, Tuner, DvdPlayer, Projector, TheaterLights, Screen, PopcornPopper, HomeTheaterFacade

if __name__ == "__main__":
    # Create Subsystem components
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    projector = Projector()
    lights = TheaterLights()
    screen = Screen()
    popper = PopcornPopper()

    # Create the Facade
    home_theater = HomeTheaterFacade(amp, tuner, dvd, projector, lights, screen, popper)

    # Use the Facade
    print("--- Movie Time ---")
    home_theater.watch_movie("Inception")

    print("\n" + "="*30 + "\n")

    print("--- End of Movie ---")
    home_theater.end_movie()
