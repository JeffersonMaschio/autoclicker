import customtkinter as ctk

class FrameCursorPosition(ctk.CTkFrame):
    def __init__(self, master, cores, fontes, **kwargs):
        super().__init__(master, height=100, fg_color=cores["frameBg"], border_color=cores["border"], border_width=1, **kwargs)
        self.cores = cores
        self.fontes = fontes
        self._criarWidgets()

    def _criarWidgets(self):
        labelTitulo = ctk.CTkLabel(self, text="[ Cursor Position ]", font=self.fontes["titulo"], text_color=self.cores["text"])
        labelTitulo.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

        self.takePosition = self._criarCheckbox(row=1, texto="Current Mouse Position", padyExtra=5)
        self.setPosition = self._criarCheckbox(row=2, texto="Set Location", padyExtra=(5, 7))

    def _criarCheckbox(self, row, texto, padyExtra):
        chb = ctk.CTkCheckBox(
            self, text=texto, border_width=1.5, text_color=self.cores["text"],
            hover_color=self.cores["hover"], fg_color=self.cores["text"], checkmark_color=self.cores["checkmark"]
        )
        chb.grid(row=row, column=0, padx=(10, 0), pady=padyExtra, sticky="w")
        return chb

    def obterValores(self):
        return {
            "currentMousePosition": bool(self.takePosition.get()),
            "setLocation": bool(self.setPosition.get()),
        }
