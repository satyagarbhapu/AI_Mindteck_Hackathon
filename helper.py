

import re

def clean_llm_output(text: str) -> str:
    """
    Removes markdown code blocks safely.
    """
    text = text.replace("```python", "")
    text = text.replace("```", "")
    return text.strip()


def extract_python_code(text: str) -> str:
    """
    Extracts Python code from LLM output.
    Handles cases like:
    - ```python ... ```
    - ``` ... ```
    - mixed text before/after code blocks
    """

    if not text:
        return ""

    # Case 1: explicit ```python blocks
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)

    if matches:
        return "\n\n".join(match.strip() for match in matches)

    # Case 2: generic ``` blocks
    pattern = r"```(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)

    if matches:
        return "\n\n".join(match.strip() for match in matches)

    # Case 3: fallback (no markdown found → return raw text)
    return text.strip()
