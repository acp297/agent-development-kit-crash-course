import os

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool

from manager_agent.sub_agents.funny_nerd.agent import funny_nerd
from manager_agent.sub_agents.news_analyst.agent import news_analyst
from manager_agent.sub_agents.stock_analyst.agent import stock_analyst
from manager_agent.tool_agents.tools import get_current_time

model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

root_agent = Agent(
    model=model,
    name="manager_agent",
    description="Manager agent",
    instruction="""
        You are a manager agent that is responsible for overseeing the work of the other agents.

        Always delegate the task to the appropriate agent. Use your best judgement 
        to determine which agent to delegate to.

        You are responsible for delegating tasks to the following agent:
        - stock_analyst
        - funny_nerd

        You also have access to the following tools:
        - news_analyst
        - get_current_time
        """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],

)