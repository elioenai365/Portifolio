# 🔍 Automação de Extração e Verificação de Perfis / Chats (FantariasOnline)

Script em Python utilizando **Playwright Async** para automação web, raspagem de dados e busca reversa de imagens no **Yandex Images**. O objetivo é extrair fotos de perfil/carrossel e mídias enviadas no chat de conversas (mesmo as cobertas por desfoque/spoiler), realizar o download e abrir automaticamente buscas de verificação de autenticidade no Yandex.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Playwright (Async API)**: Navegação automatizada e interceptação de requisições de rede.
* **Urllib (parse/unquote)**: Decodificação de parâmetros de URL e codificação para buscas.
* **Yandex Images API/Search**: Pesquisa reversa para verificação de perfis e imagens idênticas na web.

---

## 📌 Funcionalidades Desenvolvidas

### 1. Autenticação e Persistência de Sessão
* Reutilização de tokens e cookies via arquivo `session_state.json` gerado pelo script de login prévio, evitando reautenticações desnecessárias.

### 2. Extração de Carrossel de Fotos de Perfil
* Navegação sequencial pelo carrossel do perfil (`MAX_FOTOS_CARROSSEL`).
* Clique automático em botões de navegação lateral (`lucide-chevron-right`, `button.embla__next`, etc.).
* Evita fotos duplicadas armazenando URLs já processadas em um `set()`.

### 3. Revelação de Mídias Ocultas/Desfocadas no Chat
* Detecção automática de mídias enviadas na conversa cobertas por camadas de desfoque ou overlay de segurança (`backdrop-blur-xl`, ícone `lucide-eye`).
* Clique automático para remoção da camada desfoque/spoiler e carregamento do recurso em alta definição antes do download.

### 4. Normalização e Decodificação de URLs Otimizadas (Next.js & AWS S3)
* Tratamento de links no formato otimizado do Next.js (`/_next/image?url=...`).
* Decodificação de parâmetros URL encode (`%3A%2F%2F`) para extrair os links diretos e limpos do bucket **Amazon S3** (`s3-venus.s3.us-east-2.amazonaws.com`).

### 5. Download Local e Busca Reversa Automatizada
* Salvamento das imagens na pasta local `./downloads_perfil`.
* Abertura de abas separadas no navegador com a busca reversa pronta no Yandex (`yandex.com/images/search?rpt=imageview&url=...`).
* Pausa interativa para análise e fechamento ordenado das abas para economia de memória RAM.

---

## 🚀 Como Executar o Projeto

### Prerequisitos
Certifique-se de ter o Python e as dependências instaladas:

```bash
pip install playwright
playwright install chromium