import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


model = LiteLlm(
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    # model="gemini-2.0-flash",
    model=model,
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    Make sure you greet them by saying Hoo La La. 
    """,
)

