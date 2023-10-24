### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nurlan-Aliev/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Nurlan-Aliev/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e845923d5fca1eb63da6/maintainability)](https://codeclimate.com/github/Nurlan-Aliev/python-project-52/maintainability)


# Welcome to [Task Manager](https://task-manager-o9zw.onrender.com)

## Description 
Task Manager is a powerful tool designed to simplify and organize your workflow. It's software that helps you manage tasks effectively, set priorities, and collaborate with a team.
It allows you to set tasks, assign performers and change their statuses. To work with the system, registration and authentication are required.


## Key Features 
* Task Creation: You can easily create new tasks and specify details such as title, description, assigned individuals, and priority.
* Collaboration and Teamwork: The Task Manager provides an opportunity to collaborate with other team members. You can delegate tasks.

* Sort the list of tasks by
  * Status 
  * Executor
  * Label


## Install

1. Clone this repo
    ```bash
    git clone https://github.com/Nurlan-Aliev/python-project-52.git  
    ```
   
2. Install dependencies by poetry install
   ```bash
   poetry install
   ```
  
3. Create an env file with the following content
   ```commandline
   SECRET_KEY = your_super_strong_and_cool_secret_key
   
   SECRET_TOKEN_ROLLBAR = token_that_gives_rollbar
   ```
4. Run command make start to start
   ```bash
   make start
   ```

# Docker
1. Clone this repo
    ```bash
    git clone https://github.com/Nurlan-Aliev/python-project-52.git  
    ```

2. Run for build image and create container
    ```bash
   docker-compose up
   ```
3. Run migrate in new window 
    ```bash
   docker-cmpose run task-manager make migrate
   ```



## Build with

* Python
* Django
* Bootstrap
* Jinja2
* Requests
* Flake8
