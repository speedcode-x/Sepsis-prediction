#set up base image for the container
FROM python:3.11.5

#create a work directory in the container
WORKDIR /app

# copy the content of requirements.txt into a temp directory in the container
COPY requirements.txt /temp/requirements.txt

#install packages in requirement.txt
RUN python -m pip install --timeout 300000 -r /temp/requirements.txt

#copy all files into the working dirctory
COPY . /app

# expose port 8077
EXPOSE 8077

#Run the FastApi application
CMD ['uvicorn', 'main:app', '--host', '0.0.0.0','--port', 8077]