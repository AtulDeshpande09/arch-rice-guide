# Nord Theme

config.load_autoconfig(False)

# Font
c.fonts.default_family = "JetBrains Mono"
c.fonts.default_size = "10pt"

# Tabs & Statusbar
c.tabs.show = "never"
c.statusbar.show = "in-mode"

# Downloads folder
c.downloads.location.directory = "~/Downloads"

# Nord Colors
c.colors.completion.fg = "#D8DEE9"
c.colors.completion.odd.bg = "#2E3440"
c.colors.completion.even.bg = "#2E3440"
c.colors.completion.category.bg = "#3B4252"
c.colors.completion.category.fg = "#ECEFF4"
c.colors.completion.item.selected.bg = "#5E81AC"
c.colors.completion.item.selected.fg = "#ECEFF4"

c.colors.statusbar.normal.bg = "#2E3440"
c.colors.statusbar.normal.fg = "#D8DEE9"
c.colors.statusbar.insert.bg = "#A3BE8C"
c.colors.statusbar.insert.fg = "#2E3440"
c.colors.statusbar.command.bg = "#3B4252"
c.colors.statusbar.command.fg = "#D8DEE9"

c.colors.tabs.bar.bg = "#2E3440"
c.colors.tabs.odd.bg = "#3B4252"
c.colors.tabs.odd.fg = "#D8DEE9"
c.colors.tabs.selected.odd.bg = "#5E81AC"
c.colors.tabs.selected.odd.fg = "#ECEFF4"



c.url.start_pages = "file:///home/path_to_homepage/homepage.html"
c.url.default_page = c.url.start_pages

config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('gh', 'home')
config.bind('<Ctrl+f>', 'scroll-page 0 0.5')
config.bind('<Ctrl+b>', 'scroll-page 0 -0.5')

c.downloads.location.directory = "~/Downloads"


