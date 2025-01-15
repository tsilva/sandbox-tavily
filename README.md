# sandbox-tavily

A sandbox project to experiment with the Tavily API.

## Setup

### Option 1: Using conda environment.yml

1. Install Miniconda (if not already installed):
   ```bash
   # Linux
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   
   # macOS
   brew install --cask miniconda
   ```

2. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate sandbox-tavily
   ```

### Option 2: Manual conda setup

1. Create environment manually:
   ```bash
   conda create -n sandbox-tavily python=3.11
   conda activate sandbox-tavily
   pip install tavily-python python-dotenv
   ```

### Configure Tavily

Set up your Tavily API key:
```bash
export TAVILY_API_KEY='your-api-key-here'
```

## Usage

Run the test script:
```bash
python test_tavily.py
```
