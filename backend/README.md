# ChunkVault-Lite FastAPI Backend

## Introduction

This is the backend for ChunkVault-Lite. The backend is built using FastAPI, and it uses Poetry for dependency management and Black for code formatting. To work on the project locally, you'll need a valid Deta Space project key stored in a `.env` file. This README will guide you through setting up your development environment.

## Prerequisites

-   Python 3.9 (Deta Requires 3.9)
-   Poetry (Dependency Management)
-   Black (Code Formatting)

## Getting Started

1.  Clone the repository:
    
    bash
    
    ```bash
    git clone https://github.com/yourusername/chunkvault-lite-backend.git
    cd chunkvault-lite-backend
    ```
    
2.  Install Poetry, if you haven't already, follow the instructions [here](https://python-poetry.org/docs/#installation).
    
3.  Install the project dependencies using Poetry:
    
    ```bash
    poetry install
    ```
    
4.  Install Black if you haven't already:
    
    ```bash
    pip install black
    ```
    
5.  Set up your `.env` file:
    
    bash
    
    ```bash
    touch .env
    ```
    
    Open the `.env` file and add your Deta Space project key as follows:
    
    makefile
    
    ```makefile
    DETA_PROJECT_KEY=<your_deta_project_key>
    ```
    
    Replace `<your_deta_project_key>` with your actual Deta Space project key.
    

## Running the Backend

1.  Activate the virtual environment:
    
    ```
    poetry shell
    ```
    
2.  Run the FastAPI server:
    
    ```bash
    poetry run start
    ```
    
    The server should now be running at `http://127.0.0.1:8080`.

## Code Formatting

To format your code using Black, run the following command:

```bash
black application
```

## Ruff as a Linter

Ruff is a powerful linter that helps ensure clean, readable, and maintainable code. To use Ruff in this project, follow the steps below:

Install Ruff if you haven't already:

```bash
pip install ruff
```

To run Ruff as a linter and automatically fix issues, use the following command:

```bash
ruff check . --fix
```

This command will check the entire project for linting issues and attempt to fix them automatically.

**Remember to run Ruff regularly to keep your code clean and maintainable.**