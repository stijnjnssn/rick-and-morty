# Project Name

Welcome to the Rick and Morty repository! This project provides a Docker container that runs the `main.py` script using the dependencies specified in `requirements.txt`.

## extra info:
main.py is the first exercise

main_second_exercise.py is the second exercise which makes use of methods from other_files.py

google_drive.py and app.py are part of the second exercise but couldn't be validated since the api call doesn't work. Contains vanilla code of the thought process.

nb: If it doesn't work to run the application in the docker container, pull the code and write:
1. ```shell
      conda create --name myenv
      conda activate myenv
      conda install --file requirements.txt
      python main.py
Feel free to make your own environment and add some dependencies yourself. 

## Try to run the docker container

1. Clone the repository:
   ```shell
   git clone https://github.com/stijnjnssn/rick-and-morty
   cd [repository directory]
   docker build -t project-name.
2. Run the docker container:
   ```shell
   docker run project-name.
   
The main.py script of exercise one will execute inside the Docker container.


   
