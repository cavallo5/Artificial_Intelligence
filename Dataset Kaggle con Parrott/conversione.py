import pandas as pd
from sklearn.model_selection import train_test_split#lettura dati da csv file
df_train = pd.read_csv('dataset/train_data_mappato.csv',error_bad_lines=False)
df_test = pd.read_csv('dataset/test_data.csv',error_bad_lines=False) 
df_bert = pd.DataFrame({'guid': df_train['sentiment'],'label': df_train['content']})#split
df_bert_train, df_bert_dev = train_test_split(df_bert, test_size=0.01)
df_bert_test = pd.DataFrame({'guid': df_test['id'],'text': df_test['content']})
df_bert_train.to_csv('dataset/train.tsv', sep='\t', index=False, header=False)#creazione train.tsv
df_bert_dev.to_csv('dataset/dev.tsv', sep='\t', index=False, header=False)#creazione dev.tsv
df_bert_test.to_csv('dataset/test.tsv', sep='\t', index=False, header=True)#creazione test.tsv