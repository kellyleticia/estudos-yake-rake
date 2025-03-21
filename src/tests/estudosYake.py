#Aqui, eu apenas testei e estudei como usar o yake.


from yake import KeywordExtractor
extractor = KeywordExtractor()
text = "A equipe de futebol entrou em campo sob uma forte aplauso da torcida. O jogador mais experiente, Paulo, liderava o time com determinação e habilidade. O jogo estava empatado quando ele recebeu a bola e avançou pela linha de defesa adversária, fazendo um golaço de fora da área. A torcida explodiu em gritos de alegria enquanto Paulo comemorava com seus companheiros de equipe."
keywords = extractor.extract_keywords(text)
print(keywords)