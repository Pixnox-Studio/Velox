from VeloxEngine import *

class Game1(GameObject):
    def __init__(self):
        super().__init__()

    def on_create(self):
        super().on_create()
        print("loaded obj 1")

    def on_update(self):
        super().on_update()
        print("updating obj 1")


class TestScene(Scene):
    def __init__(self):
        super().__init__()

    def on_create(self):
        super().on_create()

        self.game_object = Game1()

        self.add_game_object(self.game_object)

if __name__ == '__main__':
    engine = Engine()

    engine.add_scene("test",TestScene())

    engine.run()