# Feddit Comments API

## Introduction

Feddit Comments API is a FastAPI-based web API designed to analyze the sentiment of comments retrieved from Feddit API (Fake Reddit API).


## Repository Overview
This repository contains the source code and configuration files for the API. 

- `app/`: The main application folder.

  - `api/`:

    - `api_handler/`: Handles API requests.

  - `sentiment_analysis/`:

    - `classification.py`: Contains code for sentiment analysis classification.

  - `main.py`: The main FastAPI application file containing the API endpoints.

- `.dockerignore`: The .dockerignore file listing files and directories to exclude from the Docker build context.

- `docker-compose.yml`: The Docker Compose configuration file for managing the Docker containers required to run the Feddit Sentiment Analyzer, including dependencies.

- `Dockerfile`: The Dockerfile specifying the instructions for building the Docker image of the FastAPI application.

- `requirements.txt`: A file specifying Python dependencies required for running the FastAPI application.


The API can be assessed using the 'docker-compose.yml' file in the repository.


## Running with Docker
##### Prerequisite: Make sure Docker is installed.

- To locally run the API, open the terminal and replace <path-to-docker-compose.yml> with the actual path to the provided `docker-compose.yml` file in the following command:
```bash
docker-compose -f <path-to-docker-compose.yml> up -d 
```

- To stop the API, use the following command in the terminal, replacing <path-to-docker-compose.yml> with the actual path to the provided `docker-compose.yml` file:
```bash
docker-compose -f <path-to-docker-compose.yml> down
```

The application will be accessible at http://localhost:9090

## API Documentation
- Access the OpenAPI documentation: http://localhost:9090/docs
- Endpoint for sentiment analysis: http://localhost:/comments_sentiment/
