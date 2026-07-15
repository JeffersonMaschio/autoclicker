import customtkinter as ctk

class FrameClickOption(ctk.CTkFrame):
    def __init__(self, master, cores, fontes, **kwargs):
        super().__init__(master, fg_color=cores["frameBg"], border_color=cores["border"], border_width=1, **kwargs)
        self.cores = cores
        self.fontes = fontes
        self._criarWidgets()

    def _criarWidgets(self):
        labelTitulo = ctk.CTkLabel(self, text="[ Click Option ]", font=self.fontes["titulo"], text_color=self.cores["text"])
        labelTitulo.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=(3, 0))

        self.cmbMouse = self._criarOptionMenu(row=1, texto="Mouse Button", valores=["Left", "Right", "Middle"])
        self.cmbType = self._criarOptionMenu(row=2, texto="Click Type", valores=["Single", "Double"])

    def _criarOptionMenu(self, row, texto, valores):
        label = ctk.CTkLabel(self, text=texto, font=self.fontes["entry"], text_color=self.cores["text"])
        label.grid(row=row, column=0, padx=(15, 0), sticky="w")

        combo = ctk.CTkOptionMenu(
            self, values=valores, width=85,
            fg_color=self.cores["comboFg"], button_color=self.cores["buttonBg"],
            button_hover_color=self.cores["hover"], dropdown_fg_color=self.cores["dropdownBg"],
            dropdown_text_color=self.cores["text"], dropdown_font=self.fontes["entry"],
            text_color=self.cores["text"]
        )
        combo.grid(row=row, column=1, pady=5)
        return combo

    def obterValores(self):
        return {
            "mouseButton": self.cmbMouse.get(),
            "clickType": self.cmbType.get(),
        }
