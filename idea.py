

# ============================================================
# Auto Clicker UI (Wireframe)
# ============================================================
 
# +---------------------------------------------------+
# |                                                   |
# |  +------------+   +----------------------------+  |
# |  |            |   |         Click Repeat       |  |
# |  |   Click    |   +----------------------------+  |
# |  |  Interval  |   |         Click Option       |  |
# |  |            |   |                            |  |
# |  +------------+   +----------------------------+  |
# |                                                   |
# |  +---------------------------------------------+  |
# |  |              Cursor Position                |  |
# |  +---------------------------------------------+  |
# |                                                   |
# |  +---------------------------------------------+  |
# |  |         Start + Select Hotkey               |  |
# |  +---------------------------------------------+  |
# |                                                   |
# +---------------------------------------------------+

# Click Interval
# - Tempo entre cada clique.
# - Ex.: 100 ms, 500 ms, 1 s.

# Click Repeat
# - Quantidade de cliques.
# - Pode ser finito ou infinito.

# Click Option
# - Botão do mouse (Esquerdo/Direito/Meio).
# - Clique simples ou duplo.

# Cursor Position
# - Exibe as coordenadas atuais do cursor.
# - Permite registrar uma posição para clicar.

# Start + Select Hotkey
# - Seleciona uma tecla de atalho.
# - Inicia/para o autoclicker.






# ============================================================
# OP Auto Clicker 2.1 (Wireframe)
# ============================================================

#  +----------------------------------------------------------+
#  |                    OP Auto Clicker 2.1                   |
#  +----------------------------------------------------------+
#
#  Click interval
#  +----------------------------------------------------------+
#  | [0] hours | [0] mins | [0] secs | [100] milliseconds     |
#  +----------------------------------------------------------+
#
#  +---------------------------+  +---------------------------+
#  |       Click options       |  |       Click repeat        |
#  |                           |  |                           |
#  | Mouse button: [ Left ▼ ]  |  | ( ) Repeat  [ 1 ] times   |
#  |                           |  |                           |
#  | Click type:  [ Single ▼ ] |  | (●) Repeat until stopped  |
#  |                           |  |                           |
#  +---------------------------+  +---------------------------+
#
#  Cursor position
#  +----------------------------------------------------------+
#  | (●) Current location                                     |
#  |                                                          |
#  | [ Pick location ]   X:[ 0 ] Y:[ 0 ]                      |
#  +----------------------------------------------------------+
#
#  +---------------------------+  +---------------------------+
#  |        Start (F6)         |  |          Stop (F6)        |
#  +---------------------------+  +---------------------------+
#
#  +---------------------------+  +---------------------------+
#  |      Hotkey setting       |  |          Help >>>         |
#  +---------------------------+  +---------------------------+
#
# ============================================================

# Click Interval
# - Define o tempo entre cada clique.
# - O intervalo é composto por:
#     • Horas
#     • Minutos
#     • Segundos
#     • Milissegundos

# Click Options
# - Mouse Button:
#     • Left
#     • Right
#     • Middle
#
# - Click Type:
#     • Single
#     • Double

# Click Repeat
# - Define por quanto tempo o autoclicker executará.
#
# - Repeat:
#     Executa um número específico de cliques.
#
# - Repeat until stopped:
#     Continua clicando até que o usuário interrompa.

# Cursor Position
# - Current location:
#     Utiliza a posição atual do mouse.
#
# - Pick location:
#     Permite selecionar uma posição fixa na tela.
#
# - X / Y:
#     Exibe ou armazena as coordenadas da posição escolhida.

# Start (F6)
# - Inicia o autoclicker utilizando a tecla de atalho.

# Stop (F6)
# - Interrompe imediatamente a execução.

# Hotkey Setting
# - Permite alterar a tecla responsável por iniciar/parar
#   o autoclicker.

# Help
# - Abre a documentação ou informações sobre o programa.






""" 
PALETA:
    - Svelte Gray (Otimizado)

Fundo Principal (Janela): #1a1a1a (Cinza-carvão bem profundo e limpo)

Fundo dos Cards / Caixas Internas: #222222 (Um tom de cinza ligeiramente mais claro para dar profundidade aos blocos)

Linhas, Bordas e Textos Principais: #c0c0c0 (Prateado fosco com excelente nitidez)

Textos Secundários / Inputs Desativados: #7a7a7a (Cinza médio para criar hierarquia visual nas informações menores)

Fundo dos Botões (Start / Hotkey): #2e2e2e (Para destacar sutilmente a área clicável) 

===========================================================
FONTE:
    - Rubik

📐 Sugestão de Tamanhos de Texto (Hierarquia)

Como a interface do teu auto-clicker é compacta e precisa de bastante clareza, trabalhar com uma variação sutil de tamanhos é o ideal. Aqui está uma escala que casa muito bem com o estilo Svelte Gray:

    Títulos dos Cards (ex: [ Click Interval ], [ Controller ]): 13px ou 14px (Bold)

        Por que: Fica destacado o suficiente para separar as seções, sem roubar muito espaço vertical.

    Textos Principais / Rótulos (ex: Hours, Current Mouse Position, Mouse Button): 11px ou 12px (Regular)

        Por que: É o tamanho padrão ideal para leitura rápida de opções.

    Texto dentro dos Botões (ex: Start, Hotkey): 12px (Medium / Bold)

        Por que: Um pouco de peso preenche melhor o botão e indica que é uma ação.

    Números e Inputs de Texto (ex: os zeros das caixas de tempo): 11px (Regular)

        Por que: Mantém o alinhamento com as etiquetas sem estourar o tamanho das caixinhas.

🔤 Como garantir a fonte Rubik no CustomTkinter

O customtkinter (e o tkinter por baixo) depende das fontes instaladas no sistema operacional do usuário. Se o cara não tiver a fonte Rubik no PC dele, o Python vai substituir por uma padrão feia (como Arial ou Serif), quebrando o teu design.

Para garantir que todo mundo veja a fonte Rubik, a solução definitiva é empacotar o arquivo .ttf junto com o teu projeto e carregá-lo direto na memória via código.
Passo 1: Baixar a fonte

    Vá no Google Fonts e baixe a família Rubik.

    Pegue os arquivos que vai usar (por exemplo, Rubik-Regular.ttf e Rubik-Bold.ttf) e coloque na pasta do seu projeto (ex: em uma pasta chamada assets/).

Passo 2: Carregar a fonte no código (Linux / Windows)

Para fazer o Python ler o arquivo .ttf sem precisar instalar no sistema do usuário, usamos a biblioteca pyglet (ela faz exatamente isso de forma nativa e leve).

Primeiro, instale o pyglet:
Bash

pip install pyglet

Depois, adicione isso logo no início do teu código Python:
Python

import os
import customtkinter as ctk
import pyglet

# 1. Caminho para a pasta onde você salvou as fontes
font_dir = os.path.join(os.path.dirname(__file__), "assets")

# 2. Carrega as fontes direto na memória do app
pyglet.font.add_file(os.path.join(font_dir, "Rubik-Regular.ttf"))
pyglet.font.add_file(os.path.join(font_dir, "Rubik-Bold.ttf"))

# Agora o sistema reconhece o nome "Rubik" exatamente como está dentro do arquivo!

Passo 3: Aplicar nos componentes do CustomTkinter

Agora que ela tá carregada na memória, é só usar o nome "Rubik" normal nos teus widgets passados pelo argumento font:
Python

# Exemplo para Título do Card (Bold e maior)
titulo_font = ctk.CTkFont(family="Rubik", size=13, weight="bold")
label_titulo = ctk.CTkLabel(app, text="[ Click Interval ]", font=titulo_font)

# Exemplo para Texto Normal
texto_font = ctk.CTkFont(family="Rubik", size=11, weight="normal")
label_horas = ctk.CTkLabel(app, text="Hours", font=texto_font)

# Exemplo para Botão
botao_font = ctk.CTkFont(family="Rubik", size=12, weight="bold")
botao_start = ctk.CTkButton(app, text="Start", font=botao_font)

Fazendo desse jeito, quando você mandar o script ou compilar o executável para outra pessoa, basta a pasta assets ir junto que a interface vai abrir idêntica em qualquer computador, sem erro!
"""