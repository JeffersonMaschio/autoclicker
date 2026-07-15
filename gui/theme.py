import customtkinter as ctk

COLORS = {
    "bg": "#1a1a1a",
    "frameBg": "#222222",
    "border": "#c0c0c0",
    "text": "#c0c0c0",
    "hover": "#4f4f4f",
    "checkmark": "#2e2e2e",
    "comboFg": "#343638",
    "buttonBg": "#2e2e2e",
    "dropdownBg": "#1a1a1a",
}

def criarFontes():
    return {
        "titulo": ctk.CTkFont(family="Rubik", size=15, weight="bold"),
        "label": ctk.CTkFont(family="Rubik", size=12),
        "entry": ctk.CTkFont(family="Rubik", size=13),
    }
