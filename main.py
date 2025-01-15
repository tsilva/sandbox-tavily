from dotenv import load_dotenv
load_dotenv()

import json
from tavily import TavilyClient

# Step 1. Instantiating your TavilyClient
client = TavilyClient()

# Step 2. Executing a simple search query
response = client.search("Who is Leo Messi?")

# Step 3. That's it! You've done a Tavily Search!
print(json.dumps(response, indent=2))