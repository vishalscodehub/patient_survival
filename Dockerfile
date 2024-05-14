# pull python base image
FROM python:3.11

# copy application files
ADD / /

# specify working directory
WORKDIR /

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# expose port for application
EXPOSE 7860

# start fastapi application
CMD ["/bin/sh", "-c", "python app.py > /home/server.log"]