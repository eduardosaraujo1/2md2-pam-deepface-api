# Emotion API

REST API baseada em [deepface](https://github.com/serengil/deepface) com endpoint para analisar uma imagem (base64) e retornar a emoção da pessoa apresentada nela

# Endpoints

**POST /analyze** - Recebe `{"image": "data:image/jpg;base64,...}`

# Deploy em Docker

1. Instale [docker](https://www.docker.com/) em seu sistema operacional
2. Clone esse repositório através de `git clone github.com/eduardosaraujo1/2md2-pam-emotion-api`
3. Acessando a raiz do projeto pelo prompt de comando, utilize o comando `docker build -t eduardosaraujo/emotion-api .` (note o ponto no final do comando)
4. Inicie o container a partir da imagem utilizando `docker run -p 5005:8080 eduardosaraujo/emotion-api`
5. Teste a API acessando http://localhost:5005/ e verificando a resposta Hello, World!

# Deploy manual

1. Certifique-se de que `python 3.12.7` está instalado em seu sistema
2. Clone esse repositório através de `git clone github.com/eduardosaraujo1/2md2-pam-emotion-api`
3. Acesse a raiz do projeto e crie um ambiente python virtual através de `python -m venv .venv` (utlize python3 se estiver em Linux)
4. Inicie o ambiente virtual através de `.venv\Scripts\activate` para Windows ou `source .venv/bin/activate` em Linux
5. Instale as dependências utilizando `pip install -r requirements.txt` (ou requirements-windows.txt se estiver em Windows)
6. Ative o servidor executando `python main.py`
    - Caso esteja colocando em produção, utilize ` waitress-serve --host 0.0.0.0 main:app`

# Roadmap

-   [ ] Avalie se é possível simplificar requirements.txt para que instale-se apenas deepface, tf_keras, waitress, Flask e Flask-Cors dado que o resto é dependencia e seria instaldo automaticamente
