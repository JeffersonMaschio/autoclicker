import customtkinter as ctk

class FrameClickRepeat(ctk.CTkFrame):
    def __init__(self, master, cores, fontes, **kwargs):
        super().__init__(master, fg_color=cores["frameBg"], border_color=cores["border"], border_width=1, **kwargs)
        self.cores = cores
        self.fontes = fontes
        self._criarWidgets()

    def _criarWidgets(self):
        labelTitulo = ctk.CTkLabel(self, text="[ Click Repeat ]", font=self.fontes["titulo"], text_color=self.cores["text"])
        labelTitulo.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

        self.chbRepeat = self._criarCheckbox(row=1, texto="Repeat", padyExtra=5)
        self.chbRepeatStop = self._criarCheckbox(row=2, texto="Repeat until stopped", padyExtra=(5, 7))

    def _criarCheckbox(self, row, texto, padyExtra):
        chb = ctk.CTkCheckBox(
            self, text=texto, border_width=1.5, font=self.fontes["entry"],
            text_color=self.cores["text"], hover_color=self.cores["hover"],
            fg_color=self.cores["text"], checkmark_color=self.cores["checkmark"]
        )
        chb.grid(row=row, column=0, sticky="w", padx=(10, 0), pady=padyExtra)
        return chb

    def obterValores(self):
        return {
            "repeat": bool(self.chbRepeat.get()),
            "repeatUntilStopped": bool(self.chbRepeatStop.get()),
        }
