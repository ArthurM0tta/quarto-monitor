import os
import requests

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_notificacao(mensagem):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Configuração do Telegram não encontrada.")
        return

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    dados = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensagem
    }

    try:
        resposta = requests.post(
            url,
            data=dados,
            timeout=10
        )

        if resposta.ok:
            print("Notificação enviada para o Telegram.")
        else:
            print(
                "Erro ao enviar notificação:",
                resposta.text
            )

    except requests.RequestException as erro:
        print(
            "Erro de conexão com o Telegram:",
            erro
        )
