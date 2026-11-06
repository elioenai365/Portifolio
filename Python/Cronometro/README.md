# ⏱️ Cronômetro em Python no Terminal

Uma aplicação simples e eficiente de cronômetro desenvolvida em **Python** utilizando Orientação a Objetos. O programa é executado diretamente no terminal/prompt de comando e atualiza em tempo real a contagem de horas, minutos e segundos.

---

## 🚀 Sobre o Projeto

Este projeto consiste em um script Python chamado `cronometro.py` estruturado através da classe `Cronometro`. Ao ser executado (com duplo clique no arquivo `.py` ou via terminal), ele abre a janela do executável/terminal Python e inicia a contagem contínua do tempo no formato `HH:MM:SS`.

---

## 🛠️ Tecnologias e Módulos Utilizados

- **Linguagem**: [Python 3.x](https://www.python.org/)
- **Módulos Nativos**:
  - `time`: Utilizado para pausar a execução a cada segundo (`time.sleep(1)`).
  - `os`: Utilizado para limpar o terminal a cada atualização (`os.system('cls')`).

---

## 📋 Código Fonte (`cronometro.py`)

```python
import os
import time

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1

    def start(self):
        while True:
            os.system('cls')  # Para Linux/macOS utilize 'clear'
            print(self)
            self.incremento()
            time.sleep(1)

if __name__ == '__main__':
    cronometro1 = Cronometro()
    cronometro1.start()