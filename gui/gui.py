import customtkinter as ctk

app = ctk.CTk() 

largura, altura = 450, 550 

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

app.geometry(f"{largura}x{altura}+{x}+{y}")
app.minsize(largura, altura)
app.resizable(False, False)

frame = ctk.CTkFrame(app, width=450, height=550,
    fg_color="#ff50ff"
)
frame.pack(pady=(2, 2), padx=(2, 0))

#------------------
# Funcoes



#------------------
# Widgets 
# 
# 
frameTime = ctk.CTkFrame(frame, width=300, height=400,
    fg_color="#ffff10"
)
frameTime.grid(row=0, column=0)
 
# Hour
labelHour = ctk.CTkLabel(frameTime, text="Hours") 
labelHour.grid(row=0, column=0, padx=20, pady=(0, 10), sticky="w")

entryHour = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryHour.grid(row=0, column=1)
 
 
 # Minutes
labelMin = ctk.CTkLabel(frameTime, text="Minutes")
labelMin.grid(row=1, column=0, padx=20, pady=(0, 10))

entryMin = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryMin.grid(row=1, column=1)

 
# Seconds
labelSec = ctk.CTkLabel(frameTime, text="Seconds")
labelSec.grid(row=2, column=0, padx=20, pady=(0, 10))

entrySec = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entrySec.grid(row=2, column=1)


# Milisecs
labelMil = ctk.CTkLabel(frameTime, text="Milisec")
labelMil.grid(row=3, column=0, padx=20, pady=(0, 10))

entryMil = ctk.CTkEntry(frameTime, placeholder_text="0", width=50)
entryMil.grid(row=3, column=1)

#-------------

frameRepeat = ctk.CTkFrame(frame)
frameRepeat.grid(row=0, column=1)

labelRepeat = ctk.CTkLabel(frameRepeat, text="Click Repeat")
labelRepeat.grid(row=0, column=5)
 
cbRepeat = ctk.CTkCheckBox(frameRepeat, text="Repeat")
cbRepeat.grid(row=1, column=5, sticky="w")


cbRepeatStop = ctk.CTkCheckBox(frameRepeat, text="Repear until stoped")
cbRepeatStop.grid(row=2, column=5, sticky="w")



app.mainloop()
