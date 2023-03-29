# Instale as bibliotecas necessárias

#install.packages("RSQLite")
#install.packages("readxl")
#install.packages("dplyr")
#install.packages("rmarkdown")


# Conecte-se ao banco de dados
library(RSQLite)
con <- dbConnect(SQLite(), dbname = "PAPG.sqlite")

# Verifique se a tabela "configuracoes" existe
if(!dbExistsTable(con, "configuracoes")) {
  # Crie a tabela "configuracoes"
  dbExecute(con, "CREATE TABLE configuracoes (id INTEGER PRIMARY KEY AUTOINCREMENT, valor INTEGER)")
  
  # Insira o valor 1 na tabela
  dbExecute(con, "INSERT INTO configuracoes (valor) VALUES (1)")
}

# Leia o valor atual do banco de dados
valor_atual <- dbGetQuery(con, "SELECT valor FROM configuracoes")$valor[1]

# Leia o data frame do arquivo Excel
library(readxl)
df <- read_excel("C:/Users/pedro/OneDrive - Ministerio Publico do Espirito Santo/AGE/PAPJ/PAPJ.xlsx", sheet = "Form1")

# Verifique se o número de linhas do data frame é menor que do banco (situação atual)

library(rmarkdown)
library(dplyr)

print(nrow(df))

while(nrow(df) >= valor_atual) {

  
  report <- "papg.Rmd"
  
  linha <- as.character(valor_atual)
  
  cat("iterando a linha", linha)
  
  render(report, output_format = c("pdf_document", "word_document"), output_file = linha, output_dir = "./output")
  
  # Some 1 ao valor atual
  valor_atual <- valor_atual + 1
  
  # Atualize o valor no banco de dados
  dbExecute(con, paste("UPDATE configuracoes SET valor = ", valor_atual, "WHERE id = 1"))
}

# Feche a conexão com o banco de dados
dbDisconnect(con)

