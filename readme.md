# Project Name

Welcome to the Rick and Morty repository! This project provides a Docker container that runs the `main.py` script using the dependencies specified in `requirements.txt`.

## Prerequisites

To run this project, ensure that you have the following installed:

- Docker: https://docs.docker.com/engine/install/

## Getting Started



1. Clone the repository:
   ```shell
   git clone https://github.com/stijnjnssn/rick-and-morty
   cd [repository directory]
   docker build -t project-name.
2. Run the docker container:
   ```shell
   docker run project-name.
   
The main.py script will execute inside the Docker container.

If it doesn't work to run the application in the docker container, pull the code and write:
```shell
   conda create --name myenv
   conda activate myenv
   conda install --file requirements.txt
   python main.py






