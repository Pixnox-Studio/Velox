import os.path

from .config import *
from .window import Window,WINDOW_CONFIG,WINDOW_SIZE
class Engine:
    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))

        self.window = Window(self)

        self.ctx = mgl.create_context()

        self.running = True

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def render(self):
        self.window.render()

    def update(self):
        self.window.update()

    def close(self):
        self.window.close()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()
        self.close()