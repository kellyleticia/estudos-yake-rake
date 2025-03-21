#Aqui, eu apenas testei e estudei sobre como usar o rake.


# from rake_nltk import Rake
# r = Rake()
# text = "A equipe de futebol entrou em campo sob uma forte aplauso da torcida. O jogador mais experiente, Paulo, liderava o time com determinação e habilidade. O jogo estava empatado quando ele recebeu a bola e avançou pela linha de defesa adversária, fazendo um golaço de fora da área. A torcida explodiu em gritos de alegria enquanto Paulo comemorava com seus companheiros de equipe."
# r.extract_keywords_from_text(text)
# print(r.get_ranked_phrases())

#Extraindo palavras de um arquivo de texto
from rake_nltk import Rake
r = Rake()
with open("./testes_yake_rake/teste.txt", "r") as f:
    text = f.read()
r.extract_keywords_from_text(text)
print(r.get_ranked_phrases()) 