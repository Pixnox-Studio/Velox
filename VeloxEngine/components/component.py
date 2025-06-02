from ..core.config import *


class Component:
    def __init__(self):
        """this class will be the base class for other classes to inherit to become a component."""

        self.type = "UNDEFINED"

        self.initialised = False

        self.engine = None
        self.scene = None
        self.game_object = None

    def on_create(self):
        """this function will be called when this class is to be initialised"""
        self.initialised = True

    def on_event(self,event):
        pass

    def on_update(self):
        """this function is called once per frame"""
        pass

    def on_render(self):
        """this function is called after any code updates and graphics are ready to be drawn"""
        pass

    def on_close(self):
        """this function is called once before the application is closed"""