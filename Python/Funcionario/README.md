# Projeto Funcionário — Python

## 📋 Descrição

Este projeto foi desenvolvido como exercício de **Programação Orientada a Objetos (POO) em Python**.

O objetivo é criar uma classe chamada `Funcionario`, responsável por armazenar informações sobre um funcionário, suas horas trabalhadas e seu salário por hora em diferentes meses.

O projeto é dividido em dois arquivos:

* `funcionario.py` — contém a classe `Funcionario` e seus métodos.
* `teste_funcionario.py` — cria um objeto da classe e realiza testes das funcionalidades.

---

## 🎯 Objetivos

O programa deve permitir:

* Cadastrar o nome do funcionário.
* Cadastrar o e-mail do funcionário.
* Registrar as horas trabalhadas em determinado mês.
* Registrar o salário por hora referente a determinado mês.
* Calcular o salário mensal do funcionário.
* Exibir as informações cadastradas.

---

## 📁 Estrutura do projeto

```text
projeto-funcionario/
│
├── funcionario.py
├── teste_funcionario.py
└── README.md
```

---

## 🧑‍💻 Classe `Funcionario`

A classe possui os seguintes atributos:

| Atributo       | Descrição                                              |
| -------------- | ------------------------------------------------------ |
| `nome`         | Nome do funcionário                                    |
| `email`        | E-mail do funcionário                                  |
| `horas`        | Dicionário que armazena as horas trabalhadas por mês   |
| `salario_hora` | Dicionário que armazena o salário por hora de cada mês |

Os dicionários `horas` e `salario_hora` são criados vazios no método construtor.

### Exemplo

```python
funcionario = Funcionario("Matheus", "matheus@blablabla.com.br")
```

---

## ⚙️ Métodos

### `cadastro_hora(mes, horas)`

Registra a quantidade de horas trabalhadas em determinado mês.

```python
funcionario.cadastro_hora("Jan", 300)
```

### `cadastro_salario_hora(mes, valor)`

Registra o valor do salário por hora referente a determinado mês.

```python
funcionario.cadastro_salario_hora("Jan", 30)
```

### `calcula_salario(mes)`

Calcula o salário mensal multiplicando:

```text
Horas trabalhadas × Salário por hora
```

Por exemplo:

```text
300 horas × R$ 30,00 = R$ 9.000,00
```

### `__repr__()`

Retorna uma representação textual das informações do funcionário, permitindo utilizar:

```python
print(funcionario)
```

---

## 🧪 Testando o programa

No arquivo `teste_funcionario.py`, é criado um funcionário e cadastradas as informações referentes aos meses de janeiro e fevereiro.

Exemplo:

```python
from funcionario import Funcionario

funcionario = Funcionario(
    "Matheus",
    "matheus@blablabla.com.br"
)

funcionario.cadastro_hora("Jan", 300)
funcionario.cadastro_hora("Fev", 200)

funcionario.cadastro_salario_hora("Jan", 30)
funcionario.cadastro_salario_hora("Fev", 30)

print(funcionario)

print(funcionario.calcula_salario("Jan"))
print(funcionario.calcula_salario("Fev"))
```

---

## 📊 Resultado esperado

Para janeiro:

```text
300 × 30 = 9000
```

Para fevereiro:

```text
200 × 30 = 6000
```

Portanto, o programa deverá apresentar os salários:

```text
9000
6000
```

Além das informações cadastradas do funcionário.

---

## ▶️ Como executar

### 1. Abra a pasta no VS Code

Abra a pasta que contém os arquivos:

```text
funcionario.py
teste_funcionario.py
README.md
```

### 2. Abra o terminal

No VS Code:

```text
Terminal → Novo Terminal
```

### 3. Execute o arquivo de teste

No terminal, utilize:

```bash
python teste_funcionario.py
```

Caso seu computador utilize o comando `python3`, execute:

```bash
python3 teste_funcionario.py
```

---

## 🧠 Conceitos de Python utilizados

Neste exercício são trabalhados conceitos importantes de **Programação Orientada a Objetos**, como:

* Classes
* Objetos
* Método construtor `__init__`
* Atributos
* Métodos
* Dicionários
* Condicionais
* Multiplicação de valores
* Método especial `__repr__`
* Importação de classes entre arquivos

---

## 📚 Exemplo de funcionamento

O funcionário:

```text
Nome: Matheus
E-mail: matheus@blablabla.com.br
```

Possui:

```text
Janeiro:
300 horas
R$ 30,00 por hora

Fevereiro:
200 horas
R$ 30,00 por hora
```

Cálculo:

```text
Janeiro  → 300 × 30 = R$ 9.000,00
Fevereiro → 200 × 30 = R$ 6.000,00
```

---

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática de **Python e Programação Orientada a Objetos**.
