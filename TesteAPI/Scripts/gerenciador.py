import requests

class GerenciadorAPI:
    def __init__(self, apikey:str):
        self.endpoint = None
        self.apikey = apikey

    def configurar(self, titulo):
        titulo = titulo.replace(" ", "+")  # Substitui espaços por '+' para a URL
        self.endpoint = f"http://www.omdbapi.com/?t={titulo}&apikey={self.apikey}"

    def obter_dados(self):
        response = requests.get(self.endpoint)
        if response.status_code == 200:
            # print(f"✅ Dados obtidos com sucesso da API para '{self.endpoint}'")
            # print(f"Resposta da API: {response.json()}")  # Exibe os dados brutos da API para depuração
            return response.json()
        else:
            raise Exception(f"Erro ao obter dados da API: {response.status_code}")
        
        
        
        
if __name__ == '__name__':
    gerenciador = GerenciadorAPI(apikey='4123d0c1')
    gerenciador.configurar('Tarminator')
    dados = gerenciador.obter_dados()
    print(dados)