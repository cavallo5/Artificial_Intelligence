import pandas as pd #importo libreria pandas
from numpy import random,array
from sklearn.feature_extraction.text import CountVectorizer #importo CountVectorizer per vettorizzare i dati del dataset di training X
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

df = pd.read_csv('movie_review.csv') #leggo il dataset e lo salvo in df
X = df['text'] #salvo la colonna text del dataset nella variabile X
y = df['tag'] #salvo la colonna tag del dataset nella variabile y
random.seed(0)
vect=CountVectorizer(ngram_range=(1,2)) #uso ngram_range a (1,2) per considerare anche le parole composte da due termini contigui
X=vect.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3) #separo trainset da testset
#il test set è il 30% degli esempi
model = BernoulliNB() #algoritmo di apprendimento 
model.fit(X_train, y_train) #addestro il modello con fit()
p_test = model.predict(X_test) #metodo predict() per ottenere i risultati sui dati del testset
#Valuto accuratezza
errori = accuracy_score(y_test, p_test) #confronto etichette corrette dei dati di test (y_test) con le risposte elaborate dal programma (p_test)
print("accuratezza: "+str(errori))

#Modello costruito
#Creo query per classificarle tramite il modello creato 

#Analisi query
positiva='good wonderful film'
print('Query 1: '+positiva)
q=array([positiva]) 
q=vect.transform(q)
print(model.predict(q))

negativa='this film is very orrible'
print('Query 1: '+negativa)
r=array([negativa]) 
r=vect.transform(r)
print(model.predict(r))
