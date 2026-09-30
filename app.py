from flask import Flask, render_template, redirect, url_for

from monitoramento import ativar_monitoramento, desativar_monitoramento
from database import (
    obter_status,
    contar_movimentos_hoje,
    obter_ultimo_movimento,
    obter_ultimos_movimentos
)


app = Flask(__name__)


@app.route("/")
def inicio():
    status, ativacao_em = obter_status()

    movimentos_hoje = contar_movimentos_hoje()
    ultimo_movimento = obter_ultimo_movimento()
    ultimos_movimentos = obter_ultimos_movimentos()

    return render_template(
        "index.html",
        status=status,
        ativacao_em=ativacao_em,
        movimentos_hoje=movimentos_hoje,
        ultimo_movimento=ultimo_movimento,
        ultimos_movimentos=ultimos_movimentos
    )


@app.route("/ativar")
def ativar():
    ativar_monitoramento()
    return redirect(url_for("inicio"))


@app.route("/cancelar")
def cancelar():
    desativar_monitoramento()
    return redirect(url_for("inicio"))


@app.route("/desativar")
def desativar():
    desativar_monitoramento()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
