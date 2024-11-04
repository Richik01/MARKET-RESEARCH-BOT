import json
import os
import requests
from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results 
        from specific sources like Bloomberg, McKinsey, etc."""
        
        # Add specific domains you want to target
        specific_sites = "site:bloomberg.com OR site:mckinsey.com OR site:nexocode.com"
        
        # Include the sites filter in the query
        query_with_sites = f"{query} {specific_sites}"
        
        # Define payload with the filtered query
        payload = json.dumps({"q": query_with_sites})
        
        url = "https://google.serper.dev/search"
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        
        response = requests.post(url, headers=headers, data=payload)
        
        # Check if there is an 'organic' key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that; there could be an error with your Serper API key."
        
        results = response.json().get('organic', [])
        top_result_to_return = 4
        string = []
        
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", 
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)
    @tool("Search the internet to find databases")
    def db_internet(query):
        """Useful to search the internet to find databases  
        from specific sources like kaggle, huggingface, github, uci, etc."""
        
        # Add specific domains you want to target
        specific_sites = "site:kaggle.com OR site:github.com OR site:huggingface.co OR site:ics.uci.edu"
        
        # Include the sites filter in the query
        query_with_sites = f"{query} {specific_sites}"
        
        # Define payload with the filtered query
        payload = json.dumps({"q": query_with_sites})
        
        url = "https://google.serper.dev/search"
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        
        response = requests.post(url, headers=headers, data=payload)
        
        # Check if there is an 'organic' key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that; there could be an error with your Serper API key."
        
        results = response.json().get('organic', [])
        top_result_to_return = 4
        string = []
        
        for result in results[:top_result_to_return]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", 
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(string)
