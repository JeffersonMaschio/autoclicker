import os
import customtkinter as ctk
import pyglet

from theme import COLORS, criarFontes
from utils import validarNumero
from widgets.FrameClickInterval import FrameClickInterval
from widgets.FrameClickRepeat import FrameClickRepeat
from widgets.FrameClickOption import FrameClickOption
from widgets.FrameCursorPosition import FrameCursorPosition
from widgets.FrameController import FrameController


class App(ctk.CTk):
    def __init__(self):
        self._carregarFontesCustomizadas()
        super().__init__(fg_color=COLORS["bg"])

        self.fontes = criarFontes()  # só dá pra criar CTkFont depois do super().__init__()
        self._configurarJanela()
        self._criarLayout()

    def _carregarFontesCustomizadas(self):
        fontDir = os.path.join(os.path.dirname(__file__), "..", "assets")
        pyglet.font.add_file(os.path.join(fontDir, "Rubik-Regular.ttf"))
        pyglet.font.add_file(os.path.join(fontDir, "Rubik-Bold.ttf"))

    def _configurarJanela(self):
        largura, altura = 440, 315
        larguraTela = self.winfo_screenwidth()
        alturaTela = self.winfo_screenheight()
        x = (larguraTela // 2) - (largura // 2)
        y = (alturaTela // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")
        self.minsize(largura, altura)
        self.resizable(False, False)

    def _criarLayout(self):
        frame = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        frame.pack(fill="both", expand=True, pady=5, padx=5)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        vcmd = (self.register(validarNumero), "%P")

        self.frameInterval = FrameClickInterval(frame, COLORS, self.fontes, vcmd)
        self.frameInterval.grid(row=0, column=0, columnspan=2, sticky="new", padx=5, pady=5)

        frameRight = ctk.CTkFrame(frame, fg_color="transparent")
        frameRight.grid(row=1, column=1, sticky="new")
        frameRight.grid_columnconfigure(0, weight=1)

        self.frameRepeat = FrameClickRepeat(frameRight, COLORS, self.fontes)
        self.frameRepeat.grid(row=0, column=0, sticky="new", padx=5, pady=5)

        self.frameOption = FrameClickOption(frameRight, COLORS, self.fontes)
        self.frameOption.grid(row=1, column=0, sticky="new", padx=5, pady=(3, 0))

        frameLeft = ctk.CTkFrame(frame, fg_color="transparent")
        frameLeft.grid(row=1, column=0, sticky="new")
        frameLeft.grid_columnconfigure(0, weight=1)

        self.frameCursor = FrameCursorPosition(frameLeft, COLORS, self.fontes)
        self.frameCursor.grid(row=0, column=0, sticky="new", padx=5, pady=5)

        self.frameController = FrameController(
            frameLeft, COLORS, self.fontes,
            aoIniciar=self.aoClicarStart,
            aoDefinirHotkey=self.aoClicarHotkey,
        )
        self.frameController.grid(row=1, column=0, sticky="new", padx=5, pady=5)

    def aoClicarStart(self):
        # exemplo: já dá pra pegar tudo pronto, de qualquer frame
        print(self.frameInterval.obterValores())
        print(self.frameRepeat.obterValores())
        print(self.frameOption.obterValores())
        print(self.frameCursor.obterValores())

    def aoClicarHotkey(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
