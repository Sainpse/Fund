# 
FROM python:3.8

# Create Working Directory
WORKDIR /code

# Copying req file to working dir
COPY ./requirements.txt /code/requirements.txt

# Uses cache if nothing changes
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copying req file to working dir
COPY ./app /code/app

# running server exposed on port 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
