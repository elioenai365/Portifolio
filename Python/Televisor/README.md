# 📺 Televisor e Controle Remoto

Projeto desenvolvido em **Python** com o objetivo de praticar conceitos de **Programação Orientada a Objetos (POO)**.

## 📌 Sobre o projeto

O projeto simula o funcionamento básico de um televisor utilizando duas classes:

* `Televisor`
* `ControleRemoto`

A classe `ControleRemoto` recebe um objeto `Televisor` e permite controlar algumas de suas funções, como:

* Aumentar o volume;
* Diminuir o volume;
* Trocar de canal;
* Sintonizar novos canais.

Também foi criado um terceiro arquivo para realizar os testes das classes.

## 📂 Estrutura do projeto

```text
projeto/
│
├── televisor.py
├── controle_remoto.py
├── teste.py
└── README.md
```

## 🧩 Classe Televisor

A classe `Televisor` possui os seguintes atributos:

* `volume` — controla o volume da televisão;
* `canal_atual` — informa o canal que está sendo utilizado;
* `lista_de_canais` — armazena os canais sintonizados.

### Métodos

```python
aumentaVolume(valor)
```

Aumenta o volume da televisão.

```python
diminuiVolume(valor)
```

Diminui o volume, sem permitir que ele fique abaixo de `0`.

```python
trocaCanal(canal)
```

Troca para um canal que esteja sintonizado.

```python
sintonizaCanal(canal)
```

Adiciona um novo canal à lista de canais sintonizados.

## 🎮 Classe ControleRemoto

A classe `ControleRemoto` recebe uma televisão através do construtor:

```python
controle = ControleRemoto(tv)
```

A partir disso, o controle remoto consegue executar operações diretamente no objeto `Televisor`.

### Métodos

```python
aumentaVolume()
```

Aumenta o volume da televisão.

```python
diminuiVolume()
```

Diminui o volume da televisão.

```python
trocaCanal(canal)
```

Troca o canal da televisão.

```python
sintonizaCanal(canal)
```

Sintoniza um novo canal.

## 🧪 Testando o projeto

No arquivo `teste.py`, primeiro é criado o objeto da televisão:

```python
tv = Televisor()
```

Depois, o objeto do controle remoto recebe a televisão:

```python
controle = ControleRemoto(tv)
```

Exemplo:

```python
controle.sintonizaCanal(10)
controle.sintonizaCanal(20)
controle.sintonizaCanal(30)

controle.trocaCanal(20)

controle.aumentaVolume()

print("Canal atual:", tv.canal_atual)
print("Volume:", tv.volume)
print("Canais disponíveis:", tv.lista_de_canais)
```

## ▶️ Como executar

Certifique-se de ter o **Python** instalado.

No terminal, entre na pasta do projeto e execute:

```bash
python teste.py
```

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar:

* Classes e objetos;
* Atributos;
* Métodos;
* Construtores;
* Encapsulamento;
* Comunicação entre objetos;
* Importação de classes entre arquivos;
* Organização de projetos Python.

## 👨‍💻 Tecnologias utilizadas

* **Python 3**
* **Visual Studio Code**

---

**Projeto desenvolvido para fins de estudo em Programação Orientada a Objetos com Python.**
