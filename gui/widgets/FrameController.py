import customtkinter as ctk

class FrameController(ctk.CTkFrame):
    def __init__(self, master, cores, fontes, aoIniciar=None, aoDefinirHotkey=None, **kwargs):
        super().__init__(master, height=100, fg_color=cores["frameBg"], border_color=cores["border"], border_width=1, **kwargs)
        self.cores = cores
        self.fontes = fontes
        self.aoIniciar = aoIniciar
        self.aoDefinirHotkey = aoDefinirHotkey
        self._criarWidgets()

    def _criarWidgets(self):
        labelTitulo = ctk.CTkLabel(self, text="[ Controller ]", font=self.fontes["titulo"], text_color=self.cores["text"])
        labelTitulo.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

        self.startBt = self._criarBotao(row=1, texto="Start", comando=self.aoIniciar, padyExtra=(0, 5))
        self.hotkeyBt = self._criarBotao(row=2, texto="Hotkey", comando=self.aoDefinirHotkey, padyExtra=(5, 8))

    def _criarBotao(self, row, texto, comando, padyExtra):
        botao = ctk.CTkButton(
            self, text=texto, width=180, fg_color=self.cores["buttonBg"],
            hover_color=self.cores["hover"], text_color=self.cores["text"],
            border_width=1, border_color=self.cores["border"], command=comando
        )
        botao.grid(row=row, column=0, padx=(10, 0), pady=padyExtra, sticky="nse")
        return botao
