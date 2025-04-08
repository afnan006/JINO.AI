import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def call_openrouter(model: str, messages: list, temperature: float = 0.7, max_tokens: int = None):
    kwargs = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "extra_headers": {
            "HTTP-Referer": "http://localhost",  # Update if you deploy
            "X-Title": "JINO.AI"
        }
    }

    # Only include max_tokens if it's explicitly provided
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens

    response = client.chat.completions.create(**kwargs)

    return {
        "content": response.choices[0].message.content,
        "tokens": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
    }
