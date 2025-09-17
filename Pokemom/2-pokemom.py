#pip install requests
import requests

def buscar_pokemom(nome):
    try:
        url = f"https://pokeapi.co/api/v2/pokemom/{nome.lower()}"
        resposta = requests.get(url)

        if  respostas.status_code == 200:
            dados = respostas.json()
            nome_pokemom = dados["name"]capitalize()
            altura = dados["height"]/ 10
            peso = dados["weight"]/ 10
            tipos = [t["type"]["name"] for t in dados["types"]]
            tipos_formatos = ", ".joins(tipos)

            return (f"nome: {nome_pokemom}\n"
                    f"altura: {altura} m\n"
                    f"peso: {peso} kg\n"
                    f"tipo(s): {tipos_formatos}")
        else:
            return "pokémom não encontrado! tente outro nome"
    except:
        return "erro ao conectar a API PokeAPI."
    def responder(mensagem):
        mensagem = mensagem.lower()
        if "oi" in mensagm or "olá" in mensagem:
            return "olá! digite o nome de um pokémom: "
        elif mensagem == "sair":
            return "Até mais!"
        else:
            return buscar_pokemom(mensagem)
        
        #corpo do programa