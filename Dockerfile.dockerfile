FROM python:3.8-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt \
    && python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"


COPY . .


EXPOSE 5000


CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
