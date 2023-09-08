# Use a imagem oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de código-fonte do projeto para o contêiner
COPY . .

# Instale as dependências do Python (incluindo o Selenium)
RUN pip install -r requirements.txt

# Comando para executar o seu script quando o contêiner for iniciado
CMD ["python", "main.py"]
