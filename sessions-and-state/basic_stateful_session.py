import uuid

from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from question_answering_agent import question_answering_agent
from google.genai import types

load_dotenv()


in_memory_session_service = InMemorySessionService()

initial_state = {
    "user_name": "Anand Prakash",
    "user_preferences": """
        I like playing cricket.
        My favourite food is indo-chinese.
        My favorite tv show is "Money Heist".
    """
}


APP_NAME = "Anand Prakash"
USER_ID = "ACP"
SESSION_ID = str(uuid.uuid4())
stateful_session = in_memory_session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=in_memory_session_service,
)


new_message = types.Content(
    role="user", parts=[types.Part(text="What is Anand's favorite TV show?")]
)


for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = in_memory_session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")