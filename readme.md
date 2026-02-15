This agent is designed using a "Tool-as-a-Skill" architecture. By leveraging LangChain skills documentation, the agent can dynamically load instructions (skills) and documents depending on the user's intent.

### Install dependencies
```
pip install -r requirements.txt
```
### Update the user query

Open main.py and write your query inside the content field.

Use the exact document name that exists in the data/ folder

Do not include file extensions (.docx)

Example:
```
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Summarize the NVCA-Model-COI-10-1-2025",
            }
        ]
    }
)
```
### Run the agent
```
python main.py
```
