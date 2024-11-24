FROM python:3.12

WORKDIR /app

COPY requirements.txt ./

# TensorFlow requiremetns
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libxrandr2 \
    libxinerama1 \
    libxcursor1 \
    libxi6 \
    libgl1-mesa-glx && \
    apt-get clean

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy required files
COPY Analyze.py ./
COPY main.py ./

EXPOSE 8080

CMD [ "waitress-serve", "--host", "0.0.0.0", "main:app" ]