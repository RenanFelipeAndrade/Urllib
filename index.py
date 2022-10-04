from time import sleep
from src.utils import (
    encontra_trecho_com_preco,
    envia_email,
    envia_mesagem_telegram,
    retorna_texto_de_url,
    envia_mensagem_whatsapp,
)


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
            # envia_email(
            #     f"O preço está em {preco_atual}! Acesse a oferta através de: {url}"
            # )
            # envia_mensagem_whatsapp(
            #     f"O preço está em {preco_atual}! Acesse a oferta através de: {url}"
            # )
            # envia_mesagem_telegram(
            #     f"O preço está em {preco_atual}! Acesse a oferta através de: {url}"
            # )
            preco_anterior = preco_atual
        else:
            print("O preço não está no esperado ou não alterou ainda \n")
        sleep(10)


if __name__ == "__main__":
    main()
