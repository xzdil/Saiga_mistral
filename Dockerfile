FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Выполняем команду huggingface-cli
RUN huggingface-cli download TheBloke/saiga_mistral_7b-GGUF saiga_mistral_7b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False

RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Копируем все файлы в контейнер
COPY . /app/

# Команда для запуска FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
