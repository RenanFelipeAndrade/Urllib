import os
import smtplib
import urllib.request
from email.mime.text import MIMEText
from dotenv import load_dotenv
import pywhatkit
import telegram

load_dotenv()


def envia_mesagem_telegram(texto, destino=""):
    """
    Envia mensagen no telegram usando o starbuzz_bot.
    obrigatório: texto
    opcional: destino (id de chat ou nome de usuário - ex: @user_ex)
    """
    bot_api_key = os.getenv("TELEGRAM_BOT_API_KEY")
    user_id = os.getenv("TELEGRAM_USER_ID")

    if len(destino) == 0:
        destino = user_id

    bot = telegram.Bot(token=bot_api_key)
    bot.send_message(chat_id=destino, text=texto)
    print(f"Mensagem no telegram enviado para {destino}")


def envia_mensagem_whatsapp(texto, destino="+5547991724227"):
    """
    Envia mensagen no whatsapp usando o navegador.
    obrigatório: texto
    opcional: destino (número de telefone em formato internacional)
    """
    pywhatkit.sendwhatmsg_instantly(
        phone_no=destino, message=texto, close_time=2, tab_close=2, wait_time=10
    )
    print(f"Mensagem no whatsapp enviado para {destino}")


def envia_email(
    texto,
    titulo="Alerta de preço!",
    origem="fel9.renan02@gmail.com",
    destino="renan.fas02@gmail.com",
):
    """
    Envia email usando o serviços do Gmail.
    obrigatório: texto
    opcional: titulo, origem, destino (endereço de email válido)
    """
    usuario = os.getenv("GOOGLE_APP_EMAIL")
    senha = os.getenv("GOOGLE_APP_PASSWORD")

    mensagem = MIMEText(texto)
    mensagem["Subject"] = titulo
    mensagem["From"] = origem
    mensagem["To"] = destino

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(usuario, senha)
    server.sendmail(origem, [destino], mensagem.as_string())
    server.close()
    print(f"Email enviado para {destino}")


def retorna_texto_de_url(url):
    """
    Dada uma url, retorna o conteúdo em texto
    """
    pagina = urllib.request.urlopen(url)
    return pagina.read().decode("utf-8")


def encontra_trecho_com_preco(texto, tamanho_trecho=10):
    """
    Encontra o preço em dólares no texto e retorna o trecho contendo-o
    """
    posicao_simbolo_dolar = texto.index("$")
    trecho = texto[posicao_simbolo_dolar + 1 : posicao_simbolo_dolar + tamanho_trecho]

    separadores = [",", "."]
    elementos_preco = [
        char for char in trecho if char in separadores or char.isnumeric()
    ]
    return "".join(elementos_preco)
