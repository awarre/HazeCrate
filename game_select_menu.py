"""
"Creates a onscreen menu to select which game to launch."
"""
import tkinter
import tkinter.font


class GameMenu(tkinter.Tk):
    "Creates a onscreen menu to select which game to launch."
    def __init__(self):
        super().__init__()

        self.title("HazeCrate")
        self.geometry('1280x800')
        self['background'] = '#23272E'
        self.wm_attributes('-fullscreen', 'True')

    def create_game_menu(self, games: list):
        "Generates menu buttons from list of games"
        for game in games:
            GameMenuButton(
                self,
                text=game['name'],
                command=lambda game=game,
                window=self:
                set_game_selection(game, window)
            )


class GameMenuButton(tkinter.Button):
    "Button to select game."
    game_selection = []
    active_foreground = '#0d2330'
    active_background = '#90a1b7'
    default_foreground = '#46bAFD'
    default_background = '#454c5d'

    def __init__(self, master, **kw):
        tkinter.Button.__init__(self, master, **kw)
        self['font'] = tkinter.font.Font(size=5)
        self.default_background = '#454c5d'
        self['background'] = self.default_background
        self.config(fg='#46bAFD')
        self['activebackground'] = '#90a1b7'
        self.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self):
        "Change button background color on focus."
        self['background'] = self['activebackground']
        self.config(fg='#0d2330')

    def on_leave(self):
        "Revert button background color when losing focus."
        self['background'] = self.default_background
        self.config(fg='#46bAFD')


def set_game_selection(game_args: list, win: GameMenu):
    "Set button class variable for reference."
    GameMenuButton.game_selection = game_args
    win.destroy()
