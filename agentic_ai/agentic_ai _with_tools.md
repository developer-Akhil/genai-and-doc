
**What is Agentic AI?**

Agentic AI refers to an AI paradigm in which a model is designed to act as an autonomous agent capable of planning, reasoning, making decisions, and taking actions to achieve a goal, rather than only responding to single prompts.\
Agentic AI is an AI system that can independently plan, decide, and execute actions across multiple steps, often by using tools, memory, and feedback loops, to accomplish a defined objective.

**How Agentic AI Works (Conceptually)**\
An agentic system typically follows this loop:
1. Perceive – Understand the user goal and environment
2. Plan – Break the goal into steps
3. Act – Execute actions (API calls, database queries, code execution, searches)
4. Observe – Evaluate the results
5. Reflect & Adjust – Modify the plan if needed
6. Complete – Deliver the final outcome

**Tools in LangChain**\
In LangChain, tools are functions or APIs that extend the capabilities of a Large Language Model (LLM), allowing it to interact with the external world beyond its training data. Agents use these tools to perform specific tasks, such as searching the web, running code, or querying databases. 

**Core Concepts**
* Tools vs. Agents: A tool is a single utility or function. An agent is an LLM-powered system that reasons, plans, and decides which tools to use and when, in order to solve complex queries.
* Function Calling: Tools are essentially Python functions (or similar in other languages) wrapped in a special way so the LLM can understand their purpose, input schema, and expected output.
* ReAct Pattern: Agents typically follow a "Reasoning + Acting" loop, where they observe the output from a tool call and use that information to decide on the next action or formulate a final answer. 

**Types of Tools**
LangChain provides a wide array of built-in tools and integrations with various providers: 

* **ShellTool**(``from langchain_community.tools import ShellTool``)
The ShellTool in LangChain is a built-in tool that enables a language model (LLM) agent to execute shell/powershell(window) (bash) commands on the local operating system

* **DuckDuckGoSearchRun**(``from langchain_community.tools import DuckDuckGoSearchRun``)
The DuckDuckGoSearchRun tool is a utility within the LangChain framework that integrates the privacy-focused DuckDuckGo search engine into AI applications. \
It allows language models (LLMs) to perform real-time web searches and access up-to-date information.

* **BaseTool**(``from langchain.tools import BaseTool``)
In LangChain, BaseTool is the abstract base class used to define tools that an LLM can call during agent execution.\
BaseTool in LangChain is the abstract/base class that defines the standard interface for all “tools” an LLM agent can call. It specifies how a tool is named, described, validated, and executed.

BaseTool defines:
* The interface for tools
* How tool inputs are validated
* How tool execution is invoked
* How tools are described to the LLM
Agents rely on BaseTool to reason about which action to take and how to execute it.

Why BaseTool Exists

LLMs cannot:
* Access databases directly
* Call APIs on their own
* Execute Python code safely

BaseTool bridges this gap by:
* Exposing controlled capabilities
* Enforcing schemas
* Preventing arbitrary execution

