import customtkinter as ctk


app = ctk.CTk(fg_color="#222222") 

fonteTitulo = ctk.CTkFont(size=15, weight="bold")          
fonteLabel  = ctk.CTkFont(size=12)
fonteEntry  = ctk.CTkFont(family="JetBrainsMono Nerd Font Propo", size=13)   

largura, altura = 450, 320 

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

app.geometry(f"{largura}x{altura}+{x}+{y}")
app.minsize(largura, altura)
app.resizable(False, False)


frame = ctk.CTkFrame(app,
    fg_color="#d95f3b"
)
frame.pack(fill="both", expand=True, pady=10, padx=10)

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

frameTop = ctk.CTkFrame(frame, fg_color="#222222")
frameTop.grid(row=0, column=0, columnspan=2, sticky="new", padx=5, pady=5)
 
# Title Label
labelTime = ctk.CTkLabel(frameTop, text="[ Click Interval ]",
    font=fonteTitulo
)
labelTime.grid(row=0, column=0, columnspan=8, sticky="w", padx=10, pady=(3, 0))

# Hour
labelHour = ctk.CTkLabel(frameTop, text="Hours", font=fonteLabel) 
labelHour.grid(row=1, column=1)

entryHour = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd
)
entryHour.grid(row=1, column=0, padx=5, pady=5)
 
 
 # Minutes
labelMin = ctk.CTkLabel(frameTop, text="Minutes", font=fonteLabel)
labelMin.grid(row=1, column=3)

entryMin = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd
)
entryMin.grid(row=1, column=2, padx=5, pady=5)

 
# Seconds
labelSec = ctk.CTkLabel(frameTop, text="Seconds", font=fonteLabel)
labelSec.grid(row=1, column=5)

entrySec = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd
)
entrySec.grid(row=1, column=4, padx=5, pady=5)


# Milliseconds
labelMil = ctk.CTkLabel(frameTop, text="Millisec", font=fonteLabel)
labelMil.grid(row=1, column=7)

entryMil = ctk.CTkEntry(frameTop, placeholder_text="0", width=50,
    validate="key", validatecommand=vcmd
)
entryMil.grid(row=1, column=6, padx=5, pady=5)





#===================================================================================================
#FrameRight                                                                                        #
#===================================================================================================

frameRight = ctk.CTkFrame(frame, fg_color="transparent")
frameRight.grid(row=1, column=1, sticky="new")
frameRight.grid_columnconfigure(0, weight=1)  

#-------------
#FrameRepeat

frameRepeat = ctk.CTkFrame(frameRight, fg_color="#222222")
frameRepeat.grid(row=0, column=0, sticky="new", padx=5, pady=5)

labelRepeat = ctk.CTkLabel(frameRepeat, text="[ Click Repeat ]", font=fonteTitulo)
labelRepeat.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))
 
chbRepeat = ctk.CTkCheckBox(frameRepeat, text="Repeat",
    border_width=1.5,
    font=fonteLabel
)
chbRepeat.grid(row=1, column=0, sticky="w", padx=5, pady=5)


chbRepeatStop = ctk.CTkCheckBox(frameRepeat, text="Repear until stoped",
    border_width=1.5,
    font=fonteLabel
)
chbRepeatStop.grid(row=2, column=0, sticky="w", padx=5, pady=5)


#-------------
#FrameCLickOption

frameCO = ctk.CTkFrame(frameRight, fg_color="#222222")
frameCO.grid(row=2, column=0, sticky="new", padx=5, pady=(3, 0))

labelCO = ctk.CTkLabel(frameCO, text="[ Click Option ]", font=fonteTitulo)
labelCO.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

mouseLabel = ctk.CTkLabel(frameCO, text="Mouse Button", font=fonteLabel)
mouseLabel.grid(row=1, column=0, padx=(15, 0), sticky="w")

cmbMouse = ctk.CTkComboBox(frameCO,
    values=["Left", "Right", "Middle"],
    width=85
)
cmbMouse.grid(row=1, column=1, padx=(7, 0), pady=5)

typeLabel = ctk.CTkLabel(frameCO, text="Click Type", font=fonteLabel)
typeLabel.grid(row=2, column=0, padx=(15, 0), sticky="w")

cmbType = ctk.CTkComboBox(frameCO,
    values=["Single", "Double"],
    width=85
)
cmbType.grid(row=2, column=1, padx=(7, 0), pady=5)
#===================================================================================================






#===================================================================================================
#frameLeft                                                                                         #
#===================================================================================================

frameLeft = ctk.CTkFrame(frame, fg_color="transparent")
frameLeft.grid(row=1, column=0, sticky="new")
frameLeft.grid_columnconfigure(0, weight=1)  

#-------------
#FrameCursorPosition

framePosition = ctk.CTkFrame(frameLeft, height=100, fg_color="#222222")
framePosition.grid(row=1, column=0, sticky="new", padx=5, pady=5)

labelPosition = ctk.CTkLabel(framePosition, text="[ Cursor Position ]", font=fonteTitulo)
labelPosition.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0)) 

takePosition = ctk.CTkCheckBox(framePosition, text="Current Mouse Position",
    border_width=1.5
)
takePosition.grid(padx=5, pady=5, sticky="w")

setPosition = ctk.CTkCheckBox(framePosition, text="Set Location",
    border_width=1.5
)
setPosition.grid(padx=5, pady=5, sticky="w")


#-------------
#FrameStartHotkey

frameStart = ctk.CTkFrame(frameLeft, height=100, fg_color="#222222")
frameStart.grid(row=2, column=0, sticky="new", padx=5, pady=5)

startLabel = ctk.CTkLabel(frameStart, text="[ Controller ]", font=fonteTitulo)
startLabel.grid(row=0, column=0, sticky="w", padx=10, pady=(3, 0))

startBt = ctk.CTkButton(frameStart, text="Start",
    width=180
)
startBt.grid(row=1, column=0, padx=(5, 0), pady=(0,5))

hotkeyBt = ctk.CTkButton(frameStart, text="Hotkey",
    width=180
)
hotkeyBt.grid(row=2, column=0, padx=(5, 0), pady=(5, 8))



#===================================================================================================








#------------

app.mainloop()
