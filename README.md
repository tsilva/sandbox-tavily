<div align="center">
  <img src="logo.png" alt="sandbox-tavily" width="256"/>

  [![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
  [![Tavily](https://img.shields.io/badge/Tavily-API-orange.svg)](https://tavily.com/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **A sandbox for experimenting with the Tavily search API**

  [Tavily Docs](https://docs.tavily.com/) · [Get API Key](https://tavily.com/)
</div>

## Overview

This project provides a minimal setup for experimenting with the [Tavily API](https://tavily.com/), a search API service designed for AI applications. Use it as a starting point to explore Tavily's capabilities or as a template for integrating web search into your projects.

## Features

- Conda environment with Python 3.11 and all dependencies
- Simple example demonstrating the Tavily search workflow
- Environment variable support via `.env` files

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-tavily.git
cd sandbox-tavily
conda env create -f environment.yml
conda activate sandbox-tavily

# Configure your API key
cp .env.example .env
# Edit .env and add your Tavily API key

# Run the example
python main.py
```

## Installation

### Using conda (recommended)

```bash
conda env create -f environment.yml
conda activate sandbox-tavily
```

### Manual setup

```bash
conda create -n sandbox-tavily python=3.11
conda activate sandbox-tavily
pip install tavily-python python-dotenv
```

## Configuration

Set your Tavily API key using one of these methods:

**Option 1: Environment variable**
```bash
export TAVILY_API_KEY='your-api-key-here'
```

**Option 2: `.env` file**
```bash
cp .env.example .env
# Edit .env with your API key
```

Get your API key at [tavily.com](https://tavily.com/).

## Usage

The example script demonstrates the basic Tavily workflow:

```python
from dotenv import load_dotenv
load_dotenv()

from tavily import TavilyClient

# Instantiate client (uses TAVILY_API_KEY from environment)
client = TavilyClient()

# Execute a search
response = client.search("Who is Leo Messi?")

# Process the response
print(response)
```

Run it with:
```bash
python main.py
```

## License

[MIT](LICENSE)
