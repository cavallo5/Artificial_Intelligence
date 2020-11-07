import pandas as pd
df_test = pd.read_csv('bert-master/dataset/SENTIMENT/test.tsv', sep='\t')


print(df_test)

df_result = pd.read_csv('bert-master/bert_output/SENTIMENT/test_results.tsv', sep='\t', header=None)#crazione nuovo dataframe

df_map_result = pd.DataFrame({'text': df_test['text'],
    'label': df_result.idxmax(axis=1)})

print(df_map_result.sample(10))

'''
idxmax è una funzione utilizzata per restituire l'indice della prima occorrenza del massimo sull'asse richiesto. 
I valori NA / null sono esclusi. 
In questo caso, abbiamo passato 1 come asse da indicare per colonna invece che per riga.
'''