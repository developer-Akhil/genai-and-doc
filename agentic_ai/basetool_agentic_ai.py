from langchain.tools import BaseTool
from pydantic import BaseModel, Field

class AddInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")

class AddTool(BaseTool):
    name = "add_numbers"
    description = "Adds two integers"
    args_schema = AddInput

    def _run(self, a: int, b: int):
        return a + b

    async def _arun(self, a: int, b: int):
        raise NotImplementedError

from langchain.agents import initialize_agent

agent = initialize_agent(
    tools=[AddTool()],
    llm=llm,
    agent="zero-shot-react-description",
)

agent.invoke("What is 5 plus 7?")
