import os
import customtkinter as ctk
import pyglet

# 1. Caminho para a pasta das fontes
font_dir = os.path.join(os.path.dirname(__file__), "..", "assets")

# 2. Carrega as fontes direto na memória do app
pyglet.font.add_file(os.path.join(font_dir, "Rubik-Regular.ttf"))
pyglet.font.add_file(os.path.join(font_dir, "Rubik-Bold.ttf"))



app = ctk.CTk(fg_color="#1a1a1a") 

fonteTitulo = ctk.CTkFont(family="Rubik", size=15, weight="bold")          
fonteLabel  = ctk.CTkFont(family="Rubik", size=12)
fonteEntry  = ctk.CTkFont(family="Rubik", size=13)   

largura, altura = 440, 315

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

app.geometry(f"{largura}x{altura}+{x}+{y}")
app.minsize(largura, altura)
app.resizable(False, False)


frame = ctk.CTkFrame(app,
    fg_color="#1a1a1a"
)
frame.pack(fill="both", expand=True, pady=5, padx=5)

frame.grid_rowconfigure(0, weight=0)
frame.grid_rowconfigure(1, weight=0)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

#------------------
# Funcoes

def validar_numero(texto):
    # permite campo vazio (para poder apagar tudo) ou até 4 dígitos numéricos
    if texto == "":
        return True
    return texto.isdigit() and len(texto) <= 4

vcmd = (app.register(validar_numero), "%P")


#------------------
# Widgets 


#===================================================================================================
#FrameTop                                                                                          #
#===================================================================================================

frameTop = ctk.CTkFrame(frame, fg_color="#222222", border_color="#c0c0c0", border_width=1)
frameTop.grid(row=0, column=0, columnspan=2, sticky="new", padx=5, pady=5)
 
# Title Label
labelTime = ctk.CTkLabel(frameTop, text="[ Click Interval ]",
    font=fonteTitulo,
    text_color="#c0c0c0"
)
labelTime.grid(row=0, column=0, columnspan=8, sticky="w", padx=10, pady=(3, 0))

# Hour
labelHour = ctk.CTkLabel(frameTop, text="Hours", font=fonteLabel, text_color="#c0c0c0") 
labelHour.grid(row=1, column=1)

entryHour = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd, text_color="#c0c0c0"
)
entryHour.grid(row=1, column=0, padx=(5, 3), pady=5)

 # Minutes
labelMin = ctk.CTkLabel(frameTop, text="Minutes", font=fonteLabel, text_color="#c0c0c0")
labelMin.grid(row=1, column=3)

entryMin = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd, text_color="#c0c0c0"
)
entryMin.grid(row=1, column=2, padx=3, pady=5)
 
# Seconds
labelSec = ctk.CTkLabel(frameTop, text="Seconds", font=fonteLabel, text_color="#c0c0c0")
labelSec.grid(row=1, column=5)

entrySec = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd, text_color="#c0c0c0"
)
entrySec.grid(row=1, column=4, padx=3, pady=5)

# Milliseconds
labelMil = ctk.CTkLabel(frameTop, text="Millisecs", font=fonteLabel, text_color="#c0c0c0")
labelMil.grid(row=1, column=7)

entryMil = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd, text_color="#c0c0c0"
)
entryMil.grid(row=1, column=6, padx=3, pady=5)

#===================================================================================================


#===================================================================================================
#FrameRight                                                                                        #
#===================================================================================================

frameRight = ctk.CTkFrame(frame, fg_color="transparent")
frameRight.grid(row=1, column=1, sticky="new")
frameRight.grid_columnconfigure(0, weight=1)  

#-------------
#FrameRepeat

frameRepeat = ctk.CTkFrame(frameRight, fg_color="#222222", border_color="#c0c0c0", border_width=1)
frameRepeat.grid(row=0, column=0, sticky="new", padx=5, pady=5)

labelRepeat = ctk.CTkLabel(frameRepeat, text="[ Click Repeat ]", font=fonteTitulo, text_color="#c0c0c0")
labelRepeat.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))
 
chbRepeat = ctk.CTkCheckBox(frameRepeat, text="Repeat",
    border_width=1.5,
    font=fonteEntry,
    text_color="#c0c0c0",
    hover_color="#4f4f4f",
    checkmark_color="#2e2e2e",
    fg_color="#c0c0c0"
)
chbRepeat.grid(row=1, column=0, sticky="w", padx=(10, 0), pady=5)

chbRepeatStop = ctk.CTkCheckBox(frameRepeat, text="Repear until stopped",
    border_width=1.5,
    font=fonteEntry,
    text_color="#c0c0c0",
    hover_color="#4f4f4f",
    fg_color="#c0c0c0",
    checkmark_color="#2e2e2e"
)
chbRepeatStop.grid(row=2, column=0, sticky="w", padx=(10, 0), pady=(5, 7))


#-------------
#FrameCLickOption

frameCO = ctk.CTkFrame(frameRight, fg_color="#222222", border_color="#c0c0c0", border_width=1)
frameCO.grid(row=2, column=0, sticky="new", padx=5, pady=(3, 0))

labelCO = ctk.CTkLabel(frameCO, text="[ Click Option ]", font=fonteTitulo, text_color="#c0c0c0")
labelCO.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=(3, 0))

mouseLabel = ctk.CTkLabel(frameCO, text="Mouse Button", font=fonteEntry, text_color="#c0c0c0")
mouseLabel.grid(row=1, column=0, padx=(15, 0), sticky="w")

cmbMouse = ctk.CTkOptionMenu(frameCO,
    values=["Left", "Right", "Middle"],
    width=85,
    fg_color="#343638",
    button_color="#2e2e2e",
    button_hover_color="#4f4f4f",
    dropdown_fg_color="#1a1a1a",
    dropdown_text_color="#c0c0c0",
    dropdown_font=fonteEntry,
    text_color="#c0c0c0"
)
cmbMouse.grid(row=1, column=1, pady=5)

typeLabel = ctk.CTkLabel(frameCO, text="Click Type", font=fonteEntry, text_color="#c0c0c0")
typeLabel.grid(row=2, column=0, padx=(15, 0), sticky="w")

cmbType = ctk.CTkOptionMenu(frameCO,
    values=["Single", "Double"],
    width=85,
    fg_color="#343638",
    button_color="#2e2e2e",
    button_hover_color="#4f4f4f",
    dropdown_fg_color="#1a1a1a",
    dropdown_text_color="#c0c0c0",
    dropdown_font=fonteEntry,
    text_color="#c0c0c0",
)
cmbType.grid(row=2, column=1, pady=5)

#===================================================================================================


#===================================================================================================
#frameLeft                                                                                         #
#===================================================================================================

frameLeft = ctk.CTkFrame(frame, fg_color="transparent")
frameLeft.grid(row=1, column=0, sticky="new")
frameLeft.grid_columnconfigure(0, weight=1)  

#-------------
#FrameCursorPosition

framePosition = ctk.CTkFrame(frameLeft, height=100, 
    fg_color="#222222", 
    border_color="#c0c0c0", 
    border_width=1
)
framePosition.grid(row=1, column=0, sticky="new", padx=5, pady=5)

labelPosition = ctk.CTkLabel(framePosition, text="[ Cursor Position ]", font=fonteTitulo, text_color="#c0c0c0")
labelPosition.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0)) 

takePosition = ctk.CTkCheckBox(framePosition, text="Current Mouse Position",
    border_width=1.5,
    text_color="#c0c0c0",
    hover_color="#4f4f4f",
    fg_color="#c0c0c0",
    checkmark_color="#2e2e2e"
)
takePosition.grid(padx=(10, 0), pady=5, sticky="w")

setPosition = ctk.CTkCheckBox(framePosition, text="Set Location",
    border_width=1.5,
    text_color="#c0c0c0",
    hover_color="#4f4f4f",
    fg_color="#c0c0c0",
    checkmark_color="#2e2e2e"
)
setPosition.grid(padx=(10, 0), pady=(5, 7), sticky="w")


#-------------
#FrameStartHotkey

frameStart = ctk.CTkFrame(frameLeft, height=100, 
    fg_color="#222222", 
    border_color="#c0c0c0", 
    border_width=1
)

frameStart.grid(row=2, column=0, sticky="new", padx=5, pady=5)

startLabel = ctk.CTkLabel(frameStart, text="[ Controller ]", font=fonteTitulo, text_color="#c0c0c0")
startLabel.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

startBt = ctk.CTkButton(frameStart, text="Start",
    width=180,
    fg_color="#2e2e2e",
    hover_color="#4f4f4f",
    text_color="#c0c0c0",
    border_width=1,
    border_color="#c0c0c0"
)
startBt.grid(row=1, column=0, padx=(10, 0), pady=(0,5), sticky="nse")

hotkeyBt = ctk.CTkButton(frameStart, text="Hotkey",
    width=180,
    fg_color="#2e2e2e",
    hover_color="#4f4f4f",
    text_color="#c0c0c0",
    border_width=1,
    border_color="#c0c0c0"
)
hotkeyBt.grid(row=2, column=0, padx=(10, 0), pady=(5, 8), sticky="nse")



#===================================================================================================








#------------

app.mainloop()
