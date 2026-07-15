import customtkinter as ctk

class FrameClickInterval(ctk.CTkFrame):
    def __init__(self, master, cores, fontes, vcmd, **kwargs):
        super().__init__(master, fg_color=cores["frameBg"], border_color=cores["border"], border_width=1, **kwargs)
        self.cores = cores
        self.fontes = fontes
        self.vcmd = vcmd
        self._criarWidgets()

    def _criarWidgets(self):
        labelTitulo = ctk.CTkLabel(self, text="[ Click Interval ]", font=self.fontes["titulo"], text_color=self.cores["text"])
        labelTitulo.grid(row=0, column=0, columnspan=8, sticky="w", padx=10, pady=(3, 0))

        self.entryHour = self._criarCampo(row=1, col=0, texto="Hours")
        self.entryMin  = self._criarCampo(row=1, col=2, texto="Minutes")
        self.entrySec  = self._criarCampo(row=1, col=4, texto="Seconds")
        self.entryMil  = self._criarCampo(row=1, col=6, texto="Millisecs")

    def _criarCampo(self, row, col, texto):
        padxEntry = (5, 3) if col == 0 else 3
        entry = ctk.CTkEntry(
            self, placeholder_text="0", width=50,
            validate="key", validatecommand=self.vcmd, text_color=self.cores["text"]
        )
        entry.grid(row=row, column=col, padx=padxEntry, pady=5)

        label = ctk.CTkLabel(self, text=texto, font=self.fontes["label"], text_color=self.cores["text"])
        label.grid(row=row, column=col + 1)
        return entry

    def obterValores(self):
        return {
            "hours": self.entryHour.get(),
            "minutes": self.entryMin.get(),
            "seconds": self.entrySec.get(),
            "millisecs": self.entryMil.get(),
        }
