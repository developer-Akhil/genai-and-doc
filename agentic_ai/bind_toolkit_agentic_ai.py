
'''
In LangChain, bind_tools (or tool binding) is a way to connect custom tools functions, APIs, or utilities — to an LLM so that the model can call them 
directly during a conversation or reasoning process.
'''

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests


@tool
def add(a: int, b:int) -> int:
  """Given 2 numbers a and b this tool returns their sum"""
  c = a + b
  return c

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-e1b264341b9546a557fb085cdsd8d45bd5f8dsdf502ecc4355630040282b41a12d2d7",
    model_name="deepseek/deepseek-chat"
)


#print(llm.invoke('hello'))

'''
Binding a custom tool with llm.
'''

llm_with_tools = llm.bind_tools([add])

#print(llm_with_tools.invoke('hello, how are you?').content)

# llm_with_tools.invoke('can you sum 8 and 9?').content

'''
Tool message  
'''
result = llm_with_tools.invoke('can you sum 8 and 9?')


tool_result = add.invoke(result.tool_calls[0])

# print(tool_result)

'''
Human message  
'''
query = HumanMessage("can you sum 8 and 9 ?")

messages = [query]

messages.append(tool_result)

messages.append(result)

rs = llm_with_tools.invoke(messages).content

print(rs)
