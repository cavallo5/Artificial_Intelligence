import pandas as pd#read the original test data for the text and id
df_test = pd.read_csv('bert-master/dataset/CoLA/test.tsv', sep='\t')

#read the results data for the probabilities
df_result = pd.read_csv('bert-master/bert_output/CoLA/test_results.tsv', sep='\t', header=None)#create a new dataframe

df_map_result = pd.DataFrame({'index': df_test['index'],
    'sentence': df_test['sentence'],
    'label': df_result.idxmax(axis=1)})#view sample rows of the newly created dataframe

print(df_map_result.sample(10))

'''
idxmax è una funzione utilizzata per restituire l'indice della prima occorrenza del massimo sull'asse richiesto. 
I valori NA / null sono esclusi. 
In questo caso, abbiamo passato 1 come asse da indicare per colonna invece che per riga.
'''