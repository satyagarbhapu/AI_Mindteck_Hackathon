
from langchain_ollama import ChatOllama



# -----------------------------
# LLM Configuration
# -----------------------------
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)
