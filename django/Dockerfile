
FROM python

ENV PYTHONUNBUFFERED=1
WORKDIR /django

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY . . 

# CMD ["python"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]