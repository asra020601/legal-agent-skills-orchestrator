from pathlib import Path
from langchain.tools import tool

@tool
def load_skill(skill_name: str) -> str:
    """Load a skill prompt by name."""
    path = Path(f"skills/{skill_name}.txt")
    if not path.exists():
        return f"Skill '{skill_name}' not found."
    return path.read_text()