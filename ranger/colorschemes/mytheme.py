from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class MyTheme(ColorScheme):
    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        if context.in_browser:
            if context.selected:
                fg, bg, attr = 231, 27, bold
            elif context.empty:
                fg = 4
            elif context.error:
                fg = 1

        if context.in_titlebar:
            attr |= bold
            fg = 153
            bg = 23

        if context.marked:
            fg = rgb(72,252,254)  # Custom pink color for marked files

        return fg, bg, attr

