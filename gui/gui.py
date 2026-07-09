import customtkinter as ctk

app = ctk.CTk() 

largura, altura = 450, 450 

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

app.geometry(f"{largura}x{altura}+{x}+{y}")
app.minsize(largura, altura)
app.resizable(False, False)


frame = ctk.CTkFrame(app,
    fg_color="#f1503a"
)
frame.pack(fill="both", expand=True, pady=10, padx=10)

frame.grid_rowconfigure(0, weight=0)
frame.grid_rowconfigure(1, weight=0)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

#------------------
# Funcoes



#------------------
# Widgets 

#FrameTime
 
frameTime = ctk.CTkFrame(frame
    #fg_color="transparent"
)
frameTime.grid(row=0, column=0, sticky="new", padx=(5, 0), pady=(5, 0))
 
# Title Label
labelTime = ctk.CTkLabel(frameTime, text="Click Interval")
labelTime.grid(row=0, column=0, columnspan=2)

# Hour
labelHour = ctk.CTkLabel(frameTime, text="Hours") 
labelHour.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="w")

entryHour = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryHour.grid(row=1, column=1)
 
 
 # Minutes
labelMin = ctk.CTkLabel(frameTime, text="Minutes")
labelMin.grid(row=2, column=0, padx=20, pady=(0, 10))

entryMin = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryMin.grid(row=2, column=1)

 
# Seconds
labelSec = ctk.CTkLabel(frameTime, text="Seconds")
labelSec.grid(row=3, column=0, padx=20, pady=(0, 10))

entrySec = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entrySec.grid(row=3, column=1)


# Milisecs
labelMil = ctk.CTkLabel(frameTime, text="Milisec")
labelMil.grid(row=4, column=0, padx=20, pady=(0, 10))

entryMil = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryMil.grid(row=4, column=1)

#-------------
#FrameDireita (segura os dois abaixo)
frameDireita = ctk.CTkFrame(frame, fg_color="transparent")
frameDireita.grid(row=0, column=1, sticky="new")
frameDireita.grid_columnconfigure(0, weight=1)  

#-------------
#FrameRepeat

frameRepeat = ctk.CTkFrame(frameDireita)
frameRepeat.grid(row=0, column=0, sticky="new", padx=5, pady=5)

labelRepeat = ctk.CTkLabel(frameRepeat, text="Click Repeat")
labelRepeat.grid(row=0, column=5, columnspan=2)
 
chbRepeat = ctk.CTkCheckBox(frameRepeat, text="Repeat",
    border_width=1.5
)
chbRepeat.grid(row=1, column=5, sticky="w", padx=5, pady=5)


chbRepeatStop = ctk.CTkCheckBox(frameRepeat, text="Repear until stoped",
    border_width=1.5
)
chbRepeatStop.grid(row=2, column=5, sticky="w", padx=5, pady=5)


#-------------
#FrameCLickOption

frameCO = ctk.CTkFrame(frameDireita)
frameCO.grid(row=1, column=0, sticky="new", padx=5, pady=(3, 0))

mouseLabel = ctk.CTkLabel(frameCO, text="Mouse Button")
mouseLabel.grid(row=0, column=0, padx=(15, 0), sticky="w")

cmbMouse = ctk.CTkComboBox(frameCO,
    values=["Left", "Right", "Middle"],
    width=85
)
cmbMouse.grid(row=0, column=1, padx=(7, 0), pady=5)

typeLabel = ctk.CTkLabel(frameCO, text="Click Type")
typeLabel.grid(row=1, column=0, padx=(15, 0), sticky="w")

cmbType = ctk.CTkComboBox(frameCO,
    values=["Single", "Double"],
    width=85
)
cmbType.grid(row=1, column=1, padx=(7, 0), pady=5)


#-------------
#FrameCursorPosition

framePosition = ctk.CTkFrame(frame, height=100)
framePosition.grid(row=1, column=0, columnspan=2, sticky="new", padx=5, pady=(5, 0))
app.mainloop()
