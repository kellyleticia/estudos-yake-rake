"""Fiz uma matriz de confusão para comparar os termos chaves reais, que são os do dataset de keys, com os termos chaves que eu 
   encontrei usando o rake, e depois avaliei usando diferentes métricas."""


import os

keys = os.listdir('keys-20221230T130759Z-001/keys/')
pred = os.listdir('rake_pred/')
vp, fp, fn = 0, 0, 0

for x in keys:
    arquivos_keys = 'keys-20221230T130759Z-001/keys/' + x
    x = x.replace('.key', '')
    arquivos_pred = 'rake_pred/' + x + '.pred'

    with open(arquivos_keys, 'r') as f:
        reais = f.read()

    with open(arquivos_pred, 'r') as g:
        preditos = g.read().rstrip()

    reais = reais.split('\n')
    preditos = preditos.split('\n')

    for termo in reais:
        if termo in preditos:
            vp += 1
        else:
            fn += 1
    for termo in preditos:
        if termo not in reais:
            fp += 1

print('verdadeiros positivos:', vp, "- são os termos comuns entre os reais e os preditos.", '\nfalsos negativos:', fn, "- são os termos que aparecem apenas na classe de reais.", '\nfalsos positivos:', fp, "- são os termos que aparecem apenas na classe de preditos.")
#foram encontrados poucos verdadeiros positivos, e muitos falsos negativos e falsos positivos.

def precisao(vp, fp):
    p = vp / (vp + fp)
    return p
print("\nprecisão:", precisao(vp, fp))
#a precisão dá uma ênfase maior para os erros por falso positivo, então, demonstra a capacidade do modelo de identificar corretamente a maioria dos 
# termos previstos como reais.

def recall(vp, fn):
    r = vp / (vp + fn)
    return r
print("\nrecall:", recall(vp, fn))
#o recall dá maior ênfase para os erros por falso negativo, então, demonstra a capacidade do modelo de encontrar a maioria dos termos reais.

def f1_score(vp, fp, fn):
    f = 2 * precisao(vp, fp) * recall(vp, fn) / (precisao(vp, fp) + recall(vp, fn))
    return f
print("\nf1-score:", f1_score(vp, fp, fn))  
#o f1-score é uma métrica que equilibra precisão e recall.

#essas foram as porcentagens encontradas, mas para uma melhor avaliação sobre a relevância das porcentagens, é necessário estabelecer outros 
# parâmetros de comparação.