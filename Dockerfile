# start from python base image
FROM python:3.12

# change working directory
WORKDIR /code

# add requirments file to image
COPY ./requirements.txt /code/requirements.txt

#install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#add python code to image
COPY ./app /code/app

# specify default commands
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
