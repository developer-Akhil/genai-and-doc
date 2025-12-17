from langchain.tools import BaseTool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field
from typing import Type


class AddInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")


class AddTool(BaseTool):
    name: str = "add_numbers"
    description: str = "Adds two integers"
    args_schema: Type[BaseModel] = AddInput

    def _run(self, a: int, b: int):
        return str(a + b) + "hello jhgjh"

    async def _arun(self, a: int, b: int):
        raise NotImplementedError


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-e1b26ds4341b9546asfds557fb085cd8d45bd5f8f502ecc4355630040282b41a12d2d7",
    model_name="deepseek/deepseek-chat"
)

tools = [AddTool()]

agent = create_react_agent(
    model=llm,
    tools=tools
)

result = agent.invoke({
    "messages": [
        HumanMessage(content="What is 5 plus 7?")
    ]
})

print(result["messages"][-1].content)
