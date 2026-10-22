#!/usr/bin/env python

from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
import os

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


model = ChatDeepSeek(
    model="deepseek-flash",
    temperature=0,
    api_key=os.environ["deepseek_API_KEY"]
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)

# check the whole messages for the tools called
for msg in result["messages"]:
    print(type(msg).__name__)
    print(msg)
    print("-----")

