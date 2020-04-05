import pandas as pd
from sklearn import metrics
from sklearn.svm import LinearSVC
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def classifier_creator(min_df):
    """
    min_df = 10 siginifica "ignore termos que aparecem menos que 10%
    no dataset, quanto menor for este parâmetro, mais memória RAM será
    utilizada, um min_df de 11 funciona bem para uma memória RAM de 8gb
    """
    
    df = pd.read_csv("questions_csv.csv", delimiter='@')

    col = ['Nome da matéria', 'Pergunta']
    df= df[col]
    df= df[pd.notnull(df['Pergunta'])]

    df.columns=['Materia', 'Pergunta']

    df['category_id'] = df['Materia'].factorize()[0]

    cat_id_df = df[["Materia", "category_id"]].drop_duplicates().sort_values('category_id')

    cat_to_id = dict(cat_id_df.values)

    id_to_cat = dict(cat_id_df[['category_id','Materia']].values)

    tfidf = TfidfVectorizer(sublinear_tf= True, #use a logarithmic form for frequency
                        min_df = min_df, 
                        norm= 'l2', #ensure all our feature vectors have a euclidian norm of 1
                        ngram_range= (1,2), #to indicate that we want to consider both unigrams and bigrams.
                        stop_words =stopwords.words('portuguese')) #to remove all common pronouns to reduce the number of noisy features

    features = tfidf.fit_transform(df.Pergunta).toarray()

    labels = df.category_id

    X_train, X_test, y_train, y_test = train_test_split(df['Pergunta'], df['Materia'], random_state= 0)
    count_vect = CountVectorizer()

    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    clf = LinearSVC().fit(X_train_tfidf, y_train)

    def get_result(question):
        question = question.strip()
        result = clf.predict(count_vect.transform([question]))

        return result

    return get_result

if __name__ == "__main__":
    classifier = classifier_creator(min_df=11)
    print(classifier('Qual é a origem da vida?'))
    print(classifier('Qual é o resultado de 2+2?'))
