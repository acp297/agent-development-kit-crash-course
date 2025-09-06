from datetime import datetime

from google.adk.agents import Agent



def get_time()-> dict:
    """
    Get the current time in the format : HH:MM:SS
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return {"time":current_time}


root_agent = Agent(
    name="tool_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are helpful assistant that can use following tool:
    - get_time
    """,
    tools=[get_time]
)