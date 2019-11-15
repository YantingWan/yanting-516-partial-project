# Use an official Ubuntu 18.04 as a parent image
FROM ubuntu:18.04

# install python3.7
RUN apt-get -y update && apt-get install -y \
    software-properties-common \
	openssl \
	curl
	
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.7 python3-dev python3.7-dev

# CREATE and activate a new virtual environment
RUN python3.7 -m venv --without-pip ~/ENV3
RUN . ~/ENV3/bin/activate

# install the pip for the virtual environment
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.7 get-pip.py && rm get-pip.py

# Source installation of cloudmesh for developers
RUN pip install cloudmesh-installer
RUN mkdir cm && cd cm
RUN cloudmesh-installer git clone cloud && cloudmesh-installer install cloud -e
RUN cms help && cd ..

# Set the working directory to /ai_services on Docker
WORKDIR /ai_services

# Copy the current directory contents into the container at /ai_services
COPY . /ai_services

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available
EXPOSE 8000

# Run server.py when the container launches
CMD ["python","server.py"]