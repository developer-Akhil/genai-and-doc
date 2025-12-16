from langchain_core.tools import tool

# Step 1 -- create a function
def add(a,b):
  """Adding two numbers"""
  return a+b

# Step 2 -- adding data type hints
def add(a: int,b: int) -> int:
  """Multiply two numbers"""
  return a+b

# Step 3 -- adding tool decorator
@tool
def add(a: int,b: int) -> int:
  """This tool takes 2 integers and add them"""
  return a+b


def add1(a,b):
  """Adding two numbers"""
  return a*b


result = add.invoke({"a":5,"b":4})

print(result)

print(add.name)
print(add.description)
print(add.args)


print(multiply.args_schema.model_json_schema())


