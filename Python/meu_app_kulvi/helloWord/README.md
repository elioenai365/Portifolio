# Exemplo de Layout Horizontal Interativo com Kivy (`HBoxLayoutExemple`)

Este é um projeto simples desenvolvido em Python utilizando o framework **Kivy**. O aplicativo demonstra como criar um `BoxLayout` horizontal com botões coloridos gerados dinamicamente e como tratar eventos de clique (`on_press`) para identificar qual botão foi pressionado pelo usuário.

## 🚀 Funcionalidades

- **Geração Dinâmica:** Criação de 5 botões via loop `for`.
- **Estilização Aleatória:** Atribuição de cores (formato RGBA) sorteadas aleatoriamente pela biblioteca `random`.
- **Tratamento de Eventos (`bind`):** Vinculação do evento `on_press` de cada botão a um método *callback*.
- **Identificação da Instância:** Uso do parâmetro `instance` para capturar a propriedade `.text` do botão exatamente clicado e exibir no terminal.

## 🛠️ Pré-requisitos

- **Python 3.11** (versão recomendada para compatibilidade no Windows).
- **Kivy 2.3.1+**

## 📦 Instalação e Configuração

1. **Clone ou crie a pasta do projeto:**
   ```cmd
   mkdir meu_app_kivy
   cd meu_app_kivy
   Crie e ative o ambiente virtual (venv):

Windows (CMD):

DOS
py -3.11 -m venv kivy_venv
kivy_venv\Scripts\activate
Linux / macOS:

Bash
python3 -m venv kivy_venv
source kivy_venv/bin/activate
Instale as dependências:

Bash
python -m pip install --upgrade pip
python -m pip install "kivy[base]"
🖥️ Como Executar
Com o ambiente virtual ativado, execute o script do aplicativo:

Bash
python arquivo.py

📄 Licença
Projeto desenvolvido para fins de aprendizado sob a licença MIT.