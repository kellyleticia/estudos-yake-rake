# Análise Comparativa de Extração de Keywords: RAKE vs YAKE

Projeto de comparação entre os algoritmos RAKE e YAKE para extração automática de termos-chave, com avaliação quantitativa usando métricas de classificação.

<img src="https://img.shields.io/badge/Status-Concluído-brightgreen" alt="Status do Projeto">

## 📋 Descrição
- Extração de keywords de textos usando RAKE e YAKE
- Comparação com termos-chave de referência (gold standard)
- Cálculo de métricas de avaliação: Precisão, Recall e F1-Score
- Análise qualitativa dos resultados

## 🛠️ Configuração

### Pré-requisitos
- Python 3.8+
- Gerenciador de pacotes PIP

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/kellyleticia/ESTUDOS-YAKE-RAKE.git
cd ESTUDOS-YAKE-RAKE
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Execução

### Extração de Keywords
```bash
# Extrair termos com RAKE
python src/extraction/keywords_rake.py

# Extrair termos com YAKE
python src/extraction/keywords_yake.py
```

### Avaliação de Resultados
```bash
# Avaliar performance do RAKE
python src/evaluation/aplicandoRake.py

# Avaliar performance do YAKE
python src/evaluation/aplicandoYake.py
```

## 📊 Resultados Obtidos
| Métrica   | RAKE  | YAKE  |
|-----------|-------|-------|
| Precisão  | 0.32  | 0.45  |
| Recall    | 0.25  | 0.38  |
| F1-Score  | 0.28  | 0.41  |

**Principais conclusões**:  
✅ YAKE apresentou melhor performance geral  
⚠️ Ambos algoritmos tiveram alta taxa de falsos positivos  
🔍 Detalhes completos disponíveis nos scripts de avaliação

## 🗂️ Estrutura do Projeto
```
ESTUDOS-YAKE-RAKE/
├── data/               # Dados processados
├── src/                # Códigos-fonte
│   ├── extraction/     # Scripts de extração
│   └── evaluation/     # Scripts de avaliação
├── requirements.txt    # Dependências
└── README.md           # Este arquivo
```