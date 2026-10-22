#!/usr/bin/env python

import os
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-flash",
    api_key=os.environ["deepseek_API_KEY"],
)

response = llm.invoke("Explain RNA-seq normalization in 3 sentences.")

print(response.content)
