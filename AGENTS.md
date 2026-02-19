# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a sandbox project for experimenting with the Tavily API, a search API service. The project consists of a simple Python script that demonstrates basic Tavily search functionality.

## Environment Setup

This project uses conda for Python environment management:

```bash
# Create and activate the conda environment
conda env create -f environment.yml
conda activate sandbox-tavily
```

The environment includes Python 3.11 with the following key dependencies:
- `tavily-python`: The Tavily API client library
- `python-dotenv`: For loading environment variables from .env files

## Configuration

The Tavily API requires an API key. Set it as an environment variable:

```bash
export TAVILY_API_KEY='your-api-key-here'
```

Alternatively, create a `.env` file in the project root with:
```
TAVILY_API_KEY=your-api-key-here
```

## Running the Code

Execute the example script:
```bash
python main.py
```

This runs a simple search query using the Tavily API and prints the JSON response.

## Architecture Notes

- The codebase uses `python-dotenv` to load environment variables, allowing the `TavilyClient()` to automatically pick up the API key from environment variables or `.env` file
- The example demonstrates the basic three-step pattern: instantiate client, execute search, process response

## Important Instructions

- README.md must be kept up to date with any significant project changes
