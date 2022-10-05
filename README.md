# Projeto: Urllib

## Requisitos

- Poetry
- Senha de App Gmail
- [Arquivo .env](#env)

Caso não tenha instalado o poetry, [clique aqui para o guia oficial](https://python-poetry.org/docs/#installing-with-the-official-installer)

---

## Instalação

Clone o projeto:

```bash
git clone https://github.com/RenanFelipeAndrade/Urllib.git
```

Entre no diretório:

```bash
cd Urllib
```

Instale as dependências do projeto:

```bash
poetry install
```

Copie e renomeie o arquivo env de exemplo para .env:
(para mais informações, leia o tópico [env](#env))

```bash
cp example-env .env
```

Entre no shell do ambiente:

```bash
poetry shell
```

Pronto para executar!

```bash
python index.py
```

---

### Env

Estas são as variáveis de ambiente do projeto

```bash
GOOGLE_APP_EMAIL="uma conta gmail válida"
GOOGLE_APP_PASSWORD="uma senha de aplicativo do Google"
TELEGRAM_BOT_API_KEY="chave de api para bots"
TELEGRAM_USER_ID="id de usuário"
```

Para o projeto utilizar mensagens por Email, Telegram, Whatsapp, estas variáveis precisam estar definidas.

#### Links auxiliares

- Para criar uma senha de aplicativo Gmail [clique aqui](https://support.google.com/accounts/answer/185833?hl=en)
- Para conseguir uma chave de api para bot no telegram [clique aqui](https://t.me/botfather), e digite /start
- Para conseguir seu user_id [clique aqui](https://t.me/userinfobot), e digite /start
