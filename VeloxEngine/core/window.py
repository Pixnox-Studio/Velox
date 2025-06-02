from .config import *

WINDOW_SIZE = "window-size"
WINDOW_TITLE = "window-title"
WINDOW_BACKGROUND_COLOR = "window-background-color"
WINDOW_ICON = "window-icon"

WINDOW_CONFIG = {
    WINDOW_SIZE: (1080,720),
    WINDOW_TITLE: "Velox Engine",
    WINDOW_BACKGROUND_COLOR: (0.1,0.4,0.8),
    WINDOW_ICON: None,
}

class Window:
    def __init__(self,engine):
        self.engine = engine

        flags = pg.DOUBLEBUF | pg.OPENGL

        pg.display.set_mode(WINDOW_CONFIG[WINDOW_SIZE],flags=flags)
        pg.display.set_caption(WINDOW_CONFIG[WINDOW_TITLE])

        if WINDOW_CONFIG[WINDOW_ICON] is None:
            pg.display.set_icon(
                pg.image.load(os.path.join(self.engine.root, "..", "assets", "velox_icon.png")))
        else:
            pg.display.set_icon(pg.image.load(os.path.join(WINDOW_CONFIG[WINDOW_ICON])))


    def render(self):
        self.engine.ctx.clear(*WINDOW_CONFIG[WINDOW_BACKGROUND_COLOR])

        pg.display.flip()
    def update(self):
        pass

    def close(self):
        pass
