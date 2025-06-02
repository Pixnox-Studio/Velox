import os.path

from .config import *
from .window import Window
from ..scenes.scene_manager import SceneManager


class Engine:
    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))

        self.window = Window(self)
        self.scene_manager = SceneManager(self)

        self.ctx = mgl.create_context()

        self.running = True

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            self.scene_manager.on_event(event)

    def add_scene(self, name, scene):
        scene.engine = self
        scene.on_create()

        if self.scene_manager.selected_scene is None:
            self.scene_manager.selected_scene = name

        self.scene_manager.scenes[name] = scene

    def render(self):
        self.window.render()
        self.scene_manager.on_render()

    def update(self):
        self.window.update()
        self.scene_manager.on_update()

    def close(self):
        self.window.close()
        self.scene_manager.on_close()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()
        self.close()