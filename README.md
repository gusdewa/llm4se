# Demo Project: LLM for Software Engineers

This project is part of a live coding session focused on leveraging Large Language Models (LLM) and Langchain in software engineering. By the end of the session, participants will have a full system up and running, demonstrating the practical application of LLM in software development.

## Getting Started

Follow these instructions to get a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

Ensure the following software is installed:

- Python 3.9
- Docker and Docker Compose

### Installation

1. Clone the [repository](https://github.com/gusdewa/llm4se):
   ```bash
   git clone https://github.com/gusdewa/llm4se.git
   ```
2. Navigate to the project directory:
   ```bash
   cd [project_directory]
   ```
3. Run the setup script.

- for macOS / Linux users: `./setup.sh`
- for Windows users: `./setup-windows.bat`

4. The setup script will help to do the following:
- Copies sample.env to .env.
- Creates and activates a virtual environment.
- Installs Python packages from requirements.txt.
- Launches Docker containers with docker-compose up -d.
  
  Note: If failed, please do the manual setup accordingly

## Project Structure Overview

```bash
.
├── setup.sh            # Setup script for Linux/macOS
├── setup-windows.bat   # Setup script for Windows
├── llm                 # Langchain model files and pipelines
├── requirements.txt    # Python package requirements
├── Dockerfile          # Docker configuration
├── sample.env          # Sample environment file
├── api                 # FastAPI application
└── data                # Data storage
```

- llm: This directory is primarily used for Langchain pipelines and related LLM files.
- api: Contains FastAPI server configurations and endpoints.
- Other directories include utility scripts, Docker configurations, and data storage.

## Authors

[Rahadian Dewandono](https://linktr.ee/dewaonfire)
