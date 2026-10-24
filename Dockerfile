# Imagem base leve com Python 3.11
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Exibe as mensagens do Python imediatamente no terminal (sem buffer)
ENV PYTHONUNBUFFERED=1

# Copia o código da aplicação para dentro do container
COPY src/ /app/src/

# Comando executado quando o container inicia
CMD ["python", "src/main.py"]
