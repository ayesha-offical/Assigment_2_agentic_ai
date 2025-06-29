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
    name = "Dawai Information Agent",
    instructions=" You are a helpful assistant that provides information about Dawai, a healthcare platform. Answer questions based on the provided context.",
    model=model,
)


user_question = input("Please enter your question: ")


result = Runner.run_sync(aget, user_question)
print(result.final_output)