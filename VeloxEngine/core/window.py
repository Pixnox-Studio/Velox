from .config import *

WINDOW_SIZE = "window-size"
WINDOW_TITLE = "window-title"
WINDOW_BACKGROUND_COLOR = "window-background-color"
WINDOW_ICON = "window-icon"
WINDOW_VSYNC = "window-vsync"
WINDOW_FULLSCREEN = "window-fullscreen"
WINDOW_RESIZEABLE = "window-resizeable"
WINDOW_BORDERLESS = "window-borderless"

window_config = {
    WINDOW_SIZE: (1080,720),
    WINDOW_TITLE: "Velox Engine",
    WINDOW_BACKGROUND_COLOR: (0.1,0.4,0.8),
    WINDOW_ICON: None,
    WINDOW_VSYNC: False,
    WINDOW_FULLSCREEN: False,
    WINDOW_RESIZEABLE: False,
    WINDOW_BORDERLESS:False
}

class Window:
    def __init__(self,engine):
        self.engine = engine

        self.flags = pg.DOUBLEBUF | pg.OPENGL

        if window_config[WINDOW_RESIZEABLE]:
            self.flags |= pg.RESIZABLE

        if window_config[WINDOW_BORDERLESS]:
            self.flags |= pg.NOFRAME

        pg.display.set_mode(window_config[WINDOW_SIZE],flags=self.flags,vsync=window_config[WINDOW_VSYNC])
        pg.display.set_caption(window_config[WINDOW_TITLE])

        if window_config[WINDOW_ICON] is None:
            pg.display.set_icon(
                pg.image.load(os.path.join(self.engine.root, "..", "assets", "velox_icon.png")))
        else:
            pg.display.set_icon(pg.image.load(os.path.join(window_config[WINDOW_ICON])))


    def render(self):
        self.engine.ctx.clear(*window_config[WINDOW_BACKGROUND_COLOR])

        pg.display.flip()

    def update(self):
        pass

    def close(self):
        pass
