import pygame as pg


class InputHandler:
    def __init__(self):
        pg.joystick.init()
        self.joysticks = []
        for i in range(pg.joystick.get_count()):
            js = pg.joystick.Joystick(i)
            js.init()
            self.joysticks.append(js)

    def get_keys(self):
        return pg.key.get_pressed()

    def is_key_pressed(self, key):
        keys = self.get_keys()
        return keys[key]

    def get_mouse_buttons(self):
        return pg.mouse.get_pressed()

    def is_mouse_button_pressed(self, button_index):
        buttons = self.get_mouse_buttons()
        return buttons[button_index]

    def get_mouse_pos(self):
        return pg.mouse.get_pos()

    def get_joystick_count(self):
        return len(self.joysticks)

    def get_joystick(self, index=0):
        if 0 <= index < len(self.joysticks):
            return self.joysticks[index]
        return None

    def get_joystick_buttons(self, index=0):
        js = self.get_joystick(index)
        if not js:
            return []
        return [js.get_button(i) for i in range(js.get_numbuttons())]

    def get_joystick_axes(self, index=0):
        js = self.get_joystick(index)
        if not js:
            return []
        return [js.get_axis(i) for i in range(js.get_numaxes())]

    def get_joystick_hats(self, index=0):
        js = self.get_joystick(index)
        if not js:
            return []
        return [js.get_hat(i) for i in range(js.get_numhats())]


input_handler = InputHandler()
