from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv # Load environment variables from .env file
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.agents import create_agent
from langchain_classic import hub

load_dotenv()  # Load environment variables from .env file


llm= HuggingFaceEndpoint ( 
    repo_id="Qwen/Qwen3.8-27B:novita",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

search_tool=DuckDuckGoSearchRun()

# Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=[search_tool],
#     verbose=True
# )

# Step 5: Invoke
response = agent.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current population"})
print(response)

response['output']