# AutoClicker

Um autoclicker desktop feito em Python, inspirado no [OP Auto Clicker](https://opautoclicker.com), com interface gráfica construída em CustomTkinter.

> ⚠️ Projeto em desenvolvimento inicial. A lógica de clique e a GUI ainda estão sendo construídas — este README descreve o objetivo e a arquitetura planejada do projeto.

## Sobre o projeto

O objetivo é criar um autoclicker multiplataforma com uma interface simples e configurável, permitindo:

- **Click Interval** — definir o intervalo entre cliques (horas, minutos, segundos, milissegundos)
- **Click Options** — escolher o botão do mouse (esquerdo, direito, meio) e o tipo de clique (simples ou duplo)
- **Click Repeat** — repetir um número específico de vezes ou até ser interrompido manualmente
- **Cursor Position** — usar a posição atual do cursor ou fixar uma posição na tela (X, Y)
- **Hotkey** — iniciar/parar o autoclicker através de uma tecla de atalho configurável

O wireframe completo da interface (baseado no OP Auto Clicker) está documentado em [`idea.py`](./idea.py).

## Tecnologias

- **Python 3**
- **[pynput](https://pypi.org/project/pynput/)** — captura de eventos de mouse/teclado e simulação de cliques
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** — interface gráfica

## Estrutura do repositório

```
autoclicker/
├── gui/                  # Interface gráfica (CustomTkinter)
├── idea.py               # Wireframe e planejamento da UI (documentação)
└── main.py               # Protótipo inicial (listener de mouse com pynput)
```

## Como rodar

```bash
git clone https://github.com/JeffersonMaschio/autoclicker.git
cd autoclicker
pip install requirements.txt 
python main.py
```

## Roadmap

- [ ] Implementar a lógica de clique automático (intervalo, repetição, botão do mouse)
- [ ] Construir a GUI em CustomTkinter seguindo o wireframe
- [ ] Suporte a hotkey configurável para iniciar/parar
- [ ] Seleção de posição fixa do cursor (pick location)
- [ ] Empacotamento do executável (PyInstaller)

## Autor

Desenvolvido por [Jefferson Maschio](https://github.com/JeffersonMaschio).
