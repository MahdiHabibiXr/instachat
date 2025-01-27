FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app/app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]