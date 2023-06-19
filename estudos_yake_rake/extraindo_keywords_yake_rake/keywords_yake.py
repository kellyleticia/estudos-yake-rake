#Com o uso do yake, eu extrai termos chaves do dataset de textos, e então criei um novo dataset de termos chaves (yake_pred).


import os
from yake import KeywordExtractor

diretorio = os.listdir('docsutf8-20221230T130710Z-001/docsutf8/')
extrator= KeywordExtractor(n = 5, top = 40)

for x in diretorio:
    arquivo_texto = "docsutf8-20221230T130710Z-001/docsutf8/" + x

    with open(arquivo_texto, "r") as f:
        conteudo = f.read()
        keywords = extrator.extract_keywords(conteudo)

        palavras_chave = []
        for y in keywords:
            keyword = y[0]
            palavras_chave.append(keyword + "\n")
            
        nome_arquivo = f'{x}'.rstrip(".txt") + ".pred"
        with open(nome_arquivo, 'w') as arquivo_pred:
            for z in palavras_chave:
                arquivo_pred.write(z)                          