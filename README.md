# AutoClicker

Um autoclicker para desktop escrito em Python, inspirado no **OP Auto Clicker**. O projeto está em estágio inicial de desenvolvimento, com a interface e as funcionalidades ainda sendo planejadas e implementadas.

## 📌 Status atual

Este repositório ainda está em fase de prototipagem:

- `main.py` — teste inicial com a biblioteca `pynput`, capturando e imprimindo a posição do cursor do mouse em tempo real.
- `idea.py` — documento de planejamento com wireframes em ASCII e anotações descrevendo a interface e o funcionamento pretendido do autoclicker (baseado no layout do OP Auto Clicker 2.1).
- `gui/` — pasta reservada para a implementação da interface gráfica.
- `OP-Auto-Clicker.jpg` / `autoCLickerIdea.png` — imagens de referência visual usadas no planejamento.

## 🎯 Funcionalidades planejadas

Com base nas anotações do `idea.py`:

- **Click Interval**: definir o intervalo entre cliques (horas, minutos, segundos, milissegundos).
- **Click Options**: escolher botão do mouse (esquerdo/direito/meio) e tipo de clique (simples/duplo).
- **Click Repeat**: repetir um número fixo de vezes ou até ser interrompido manualmente.
- **Cursor Position**: usar a posição atual do mouse ou selecionar uma posição fixa na tela.
- **Hotkey**: iniciar/parar o autoclicker através de uma tecla de atalho configurável (ex.: F6).

## 🛠️ Tecnologias

- Python
- [`pynput`](https://pypi.org/project/pynput/) para captura de eventos de mouse

## 🚀 Como executar (estado atual)

```bash
pip install pynput
python main.py
```

> No momento, `main.py` apenas exibe a posição do cursor no terminal — a lógica de clique automático e a interface gráfica ainda serão implementadas.

## 📄 Licença

Ainda não definida.
