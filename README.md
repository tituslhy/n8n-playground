# n8n-playground
Deploying a ready-to-use open-source Docker Compose setup for rapid local AI and low-code development.

![n8n.io - Screenshot](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/main/assets/n8n-demo.gif)

## Setup
This repository uses the [uv package installer](https://docs.astral.sh/uv/pip/packages/). 

To create a virtual environment with the dependencies installed, simply type in your terminal:
```
uv sync
```

## To spin up n8n
Run:
```
docker compose up -d
```

## To spin up the forex MCP service
Run
```
python forex_tool.py
```

## Accessing the n8n workflows built
n8n allows for built workflows to be downloaded - these files can then be imported into other n8n servers. All workflows can be accessed in the `json` folder.

## Report
The repository walks through the n8n setup along with observations in the `notebooks` folder. The main notebooks are;
```
.
|- 0. n8n_walkthrough.ipynb     <- Covers how to build and run workflows on n8n
|- 1. call_n8n_api.ipynb        <- Covers how to invoke n8n workflow REST API deployments
|- 98. ngrok_setup.ipynb        <- Covers how to serve your n8n workflow to a public URL using ngrok for testing.
```

## Acknowledgements
This repository uses n8n's [self-hosted-ai-starter-it](https://github.com/n8n-io/self-hosted-ai-starter-kit) as its primary resource.

Note: I had to add a few more keys to the docker-compose.yaml file to make it work. They are:
```
    - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
    - N8N_RUNNERS_ENABLED=true
```

These keys are under the `x-n8n: &service-n8n` service.