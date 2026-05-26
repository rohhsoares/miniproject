import json


def salvar_tema(modo):
    config = {
        "tema": modo
    }

    with open("config.json", "w") as arquivo:
        json.dump(config, arquivo)


def carregar_tema():
    try:
        with open("config.json", "r") as arquivo:
            config = json.load(arquivo)
            return config["tema"]

    except:
        return "dark"