import customtkinter as ctk

app = ctk.CTk() 

largura, altura = 350, 450 

largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

app.geometry(f"{largura}x{altura}+{x}+{y}")
app.minsize(largura, altura)
app.resizable(False, False)

frame = ctk.CTkFrame(app, width=largura, height=altura,
    fg_color="#ff50ff"
)
frame.grid(pady=(20, 20), padx=(20, 20))

#------------------
# Funcoes



#------------------
# Widgets 


frameTime = ctk.CTkFrame(frame, width=(largura/2))
frameTime.grid()

frame.grid(row=0, column=0, padx=10, pady=10)
# Hour
labelHour = ctk.CTkLabel(frameTime, text="Hours") 
labelHour.grid(row=0, column=0, padx=20, pady=(0, 10), sticky="w")

entryHour = ctk.CTkEntry(frameTime, placeholder_text="0")
entryHour.grid(row=0, column=1)


# Minutes
labelMin = ctk.CTkLabel(frameTime, text="Minutes")
labelMin.grid(row=1, column=0, padx=20, pady=(0, 10))

entryMin = ctk.CTkEntry(frameTime, placeholder_text="0")
entryMin.grid(row=1, column=1)


# Seconds
labelSec = ctk.CTkLabel(frameTime, text="Seconds")
labelSec.grid(row=2, column=0, padx=20, pady=(0, 10))

entrySec = ctk.CTkEntry(frameTime, placeholder_text="0")
entrySec.grid(row=2, column=1)


# Milisecs
labelMil = ctk.CTkLabel(frameTime, text="Milisec")
labelMil.grid(row=3, column=0, padx=20, pady=(0, 10))

entryMil = ctk.CTkEntry(frameTime, placeholder_text="0")
entryMil.grid(row=3, column=1)

#++++++++++++++++++++++++

#





app.mainloop()
