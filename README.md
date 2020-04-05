# Classificação de questões

## Aplicação com interface gráfica que identifica através de machine learning se uma questão pertence às materias de Física, Matemática, Química, Biologia, Literatura, Gramática, História, Geografia, Filosofia, Sociologia, Artes, Inglês ou Espanhol.

---
### Como utilizar:

`pip install scikit-learn nltk`

`git clone https://github.com/WilliamVernaschi/Classificacao-de-questoes/`

`cd Classificacao-de-questoes`

`python classification-with-gui.py`

---

### Exemplo de funcionamento

![gif](https://media1.tenor.com/images/2040f65235c3e52174b44b3602095c02/tenor.gif)

---

### Processo de criação
A criação do programa foi separada em duas partes: 

1. - A obtenção do dataset de questões através de web scraping com requests e beautiful soup 4 no site <https://www.stoodi.com.br/> que contém mais de 38000 questões (URL_getter.py e csv_creator.py)

2. - A manipulação dos dados com machine learning através do Scikit-learn e NLTK. (classification.py e classification-with-gui.py)

---

### Dados adicionais
**Gráfico representando a quantidade de questões de cada matéria no dataset**

![plot](https://i.imgur.com/cxiwIPf.png)

**Precisão no acerto das questões:**
| Matéria           | Precisão |
|-------------------|----------|
| Inglês            | 100%     |
| Matemática        | 97%      |
| Espanhol          | 96%      |
| História          | 91%      |        
| Biologia          | 88%      |
| Geografia         | 85%      |         
| Química           | 83%      |
| Física            | 75%      |
| Literatura        | 69%      |
| Filosofia         | 69%      |
| Sociologia        | 60%      |
| Gramática         | 54%      |
| Artes             | 37%      |
| Média aritimética | 84%      |

---

### Fontes

<https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f>
