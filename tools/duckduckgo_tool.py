from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()
results=search_tool.invoke('who is narendra modi')

print(results)