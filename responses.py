


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("oi", "ola", "olá"):
        return "Olá Seja bem vindo ao bot do Luiz Miguel.\n digite /help para ver os comandos disponíveis"
    elif "teste" in user_message:
        return "estou funcionando"
    elif "quem é vc ?" in user_message:
        return "eu sou o bot do luiz"
   

    return "não estou entendendo você! tente novamente."