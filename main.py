from llm_initialize import llm
from langchain.agents import create_agent
from tools.load_document import load_document
from tools.load_skill import load_skill

from prompts import SYSTEM_PROMPT
agent = create_agent(
    model=llm,
    tools=[load_document, load_skill],
    system_prompt = (SYSTEM_PROMPT))


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": ("summarize the NVCA-Model-COI-10-1-2025"

                ),
            }
        ]
    }
)


print(result)
final_answer = result["messages"][-1].content
print(final_answer)
for msg in result["messages"]:
    if hasattr(msg, "tool_calls") and msg.tool_calls:
        print("Tool(s) called:")
        for call in msg.tool_calls:
            print(f"- Tool name: {call['name']}")
            print(f"  Arguments: {call['args']}")