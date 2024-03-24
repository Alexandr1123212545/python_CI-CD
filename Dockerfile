FROM python:3.12.2-alpine3.19
ENV FLASK_DEBUG=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 db.py -a
EXPOSE 5000
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000"]
