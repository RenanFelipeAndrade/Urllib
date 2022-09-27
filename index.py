from email.mime.text import MIMEText
import os
import smtplib
from time import sleep
import urllib.request
from dotenv import load_dotenv

load_dotenv()


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
    usuario = os.environ.get("GOOGLE_APP_EMAIL")
    senha = os.environ.get("GOOGLE_APP_PASSWORD")

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


def main():
    def calcula_preco(url):
        """
        Utilitário para retornar preço em float
        """
        texto = retorna_texto_de_url(url)
        preco_string = encontra_trecho_com_preco(texto)
        return float(preco_string)

    urls = [
        "http://beans.itcarlow.ie/prices.html",
        "http://beans.itcarlow.ie/prices-loyalty.html",
    ]

    preco_anterior = 0
    while True:
        precos = [calcula_preco(url) for url in urls]

        url_menor_preco = urls[precos.index(min(precos))]
        url, preco_atual = url_menor_preco, min(precos)
        if preco_atual <= 4.7 and preco_atual != preco_anterior:
            envia_email(
                f"O preço está em {preco_atual}! Acesse a oferta através de: {url}"
            )
            preco_anterior = preco_atual
        else:
            print("O preço não está no esperado ou não alterou ainda \n")
        sleep(2)


if __name__ == "__main__":
    main()
