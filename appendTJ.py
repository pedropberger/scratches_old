import pandas as pd

# read the csv file
# clean missing data
# categorize Origem
# categorize Situação

df1 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\ARQUIVADOS - SISTEMA SEGUNDA INSTÂNCIA (COMPLEMENTO).xlsx', engine='openpyxl')
#df1 = df1.dropna(axis='rows', how = 'all')
#df1 = df1.dropna(axis='columns', how = 'all')
df1['Origem'] = str('SISTEMA SEGUNDA INSTÂNCIA')
df1['Situacao_file'] = str('ARQUIVADO')

df2 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\ARQUIVADOS PJE -1GRAU ( COMPLEMENTO).xlsx', engine='openpyxl')
#df2 = df2.dropna(axis='rows', how = 'all')
#df2 = df2.dropna(axis='columns', how = 'all')
df2['Origem'] = str('PJE')
df2['Situacao_file'] = str('ARQUIVADO')

df3 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\ARQUIVADOS SISTEMA EJUD (COMPLEMENTO).xlsx', engine='openpyxl')
#df3 = df3.dropna(axis='rows', how = 'all')
#df3 = df3.dropna(axis='columns', how = 'all')
df3['Origem'] = str('EJUD')
df3['Situacao_file'] = str('ARQUIVADO')

df4 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA EJUD - ARQUIVADOS.xlsx', engine='openpyxl')
#df4 = df4.dropna(axis='rows', how = 'all')
#df4 = df4.dropna(axis='columns', how = 'all')
df4['Origem'] = str('EJUD')
df4['Situacao_file'] = str('ARQUIVADO')

df5 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA EJUD - ATIVOS.xlsx', engine='openpyxl')
#df5 = df5.dropna(axis='rows', how = 'all')
#df5 = df5.dropna(axis='columns', how = 'all')
df5['Origem'] = str('EJUD')
df5['Situacao_file'] = str('ATIVO')

df6 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA PJE - ARQUIVADOS.xlsx', engine='openpyxl')
#df6 = df6.dropna(axis='rows', how = 'all')
#df6 = df6.dropna(axis='columns', how = 'all')
df6['Origem'] = str('PJE')
df6['Situacao_file'] = str('ARQUIVADO')

df7 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA PJE - ATIVOS.xlsx', engine='openpyxl')
#df7 = df7.dropna(axis='rows', how = 'all')
#df7 = df7.dropna(axis='columns', how = 'all')
df7['Origem'] = str('PJE')
df7['Situacao_file'] = str('ATIVO')

df8 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA SEGUNDA INSTANCIA - ARQUIVADOS.xlsx', engine='openpyxl')
#df8 = df8.dropna(axis='rows', how = 'all')
#df8 = df8.dropna(axis='columns', how = 'all')
df8['Origem'] = str('SISTEMA SEGUNDA INSTÂNCIA')
df8['Situacao_file'] = str('ARQUIVADO')

df9 = pd.read_excel(r'\\sumoto\Dados\NUPROC\TJ\SISTEMA SEGUNDA INSTANCIA - ATIVOS.xlsx', engine='openpyxl')
#df9 = df9.dropna(axis='rows', how = 'all')
#df9 = df9.dropna(axis='columns', how = 'all')
df9['Origem'] = str('SISTEMA SEGUNDA INSTÂNCIA')
df9['Situacao_file'] = str('ATIVO')

#Append all

df_final = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9])
df_final = df_final.dropna(axis='rows', how = 'all')
df_final = df_final.dropna(axis='columns', thresh = 20)

#print(df_final)

df_final.to_excel(r'\\sumoto\Dados\NUPROC\TJ\TJ.xlsx')