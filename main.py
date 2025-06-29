import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel 

load_dotenv()
gemeni_api_key = os.getenv('GEMINI_API_KEY')


provider = AsyncOpenAI(
    api_key = gemeni_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider,
)

aget = Agent(
    name = "Code helper",
    instructions=" You are a helpful coding assistant. Answer the user's questions about programming and provide code examples when necessary.when someone ask about rather than code or programing information so say that you can't give information on that.",
    model=model,
)

user_question = input("Please enter your question: ")

result = Runner.run_sync(aget, user_question)
print(result.final_output)