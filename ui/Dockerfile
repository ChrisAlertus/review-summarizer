FROM ubuntu:18.04

# Set character encoding environment variables
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# Allow apt-get install without interaction from console
ENV DEBIAN_FRONTEND=noninteractive

# Set the workign directory to /root
WORKDIR /root

# System updates and configurations
RUN apt-get update && apt-get -y --no-install-recommends install \
		ca-certificates \
		git \
		ssh \
    python3 python3-virtualenv \
		wget && \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy over model and API code into the container
COPY ./app /root
COPY start.sh /root

# Pip install api requirements into the conda env
RUN pip install --upgrade pip setuptools && \
	pip install  -r /root/requirements.txt --no-cache-dir

# Make our start script executable
RUN ["chmod", "+x", "/root/start.sh"]

# Start the API
ENTRYPOINT [ "/root/start.sh" ]
