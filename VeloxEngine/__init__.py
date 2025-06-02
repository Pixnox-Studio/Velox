
# ========================================
#                  CORE
# ========================================
from .core.engine import Engine
from .core.window import (
    WINDOW_CONFIG,
    WINDOW_BACKGROUND_COLOR,
    WINDOW_SIZE,
    WINDOW_TITLE
)

# ========================================
#                SCENES
# ========================================

from .scenes.scene import Scene

# ========================================
#              GAME OBJECTS
# ========================================

from .game_objects.game_object import GameObject

# ========================================
#               COMPONENTS
# ========================================

from .components.component import Component

__all__ = [
    "Engine",
    "WINDOW_CONFIG",
    "WINDOW_BACKGROUND_COLOR",
    "WINDOW_SIZE",
    "WINDOW_TITLE",

    "Scene",

    "GameObject",

    "Component"
]