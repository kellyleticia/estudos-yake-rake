#Com o uso do rake, eu extrai termos chaves do dataset de textos, e então criei um novo dataset de termos chaves (rake_pred).


import os
from rake_nltk import Rake

diretorio = os.listdir('docsutf8-20221230T130710Z-001/docsutf8/')
r = Rake()
r.max_length = 5

for x in diretorio:
    arquivo_texto = "docsutf8-20221230T130710Z-001/docsutf8/" + x

    with open(arquivo_texto, 'r') as f:
        conteudo = f.read()
    r.extract_keywords_from_text(conteudo)
    keywords = r.get_ranked_phrases()
    keywords = keywords[:40]

    nome_arquivo = f'{x}'.rstrip(".txt") + ".pred"
    with open(nome_arquivo, 'w') as arquivo_pred:
        for keyword in keywords:
            arquivo_pred.write(keyword + '\n') 