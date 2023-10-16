# Use a base image Python
FROM python:3.8

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos (requirements.txt) para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

COPY . .

# Defina a variável de ambiente para a aplicação Flask
ENV FLASK_APP=app.py

# Exponha a porta que a aplicação Flask está ouvindo (por padrão, porta 5000)
EXPOSE 5000

# Inicialize a aplicação Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0"]