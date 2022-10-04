import os
import smtplib
import urllib.request
from email.mime.text import MIMEText
from dotenv import load_dotenv
import pywhatkit

load_dotenv()


def envia_mensagem_whatsapp(texto, destino="+5547991724227"):
    pywhatkit.sendwhatmsg_instantly(
        phone_no=destino, message=texto, close_time=2, tab_close=2, wait_time=10
    )


def envia_email(
    texto,
    titulo="Alerta de preço!",
    origem="fel9.renan02@gmail.com",
    destino="renan.fas02@gmail.com",
):
    """
    Envia email usando o serviços do Gmail.
    obrigatório: texto
    opcional: titulo, origem, destino
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
