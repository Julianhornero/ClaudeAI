
# ClaudeAI

Auto-create articles using the Anthropic Claude API with Python.

---

## Overview

ClaudeAI is a simple Python project that demonstrates how to automatically generate detailed articles using the Anthropic Claude API. By providing a text prompt, the script interacts with Claude to produce high-quality, coherent articles and saves the output locally.

---

## Features

- Generate detailed articles from any text prompt.
- Uses the official Anthropic Python SDK.
- Saves generated articles to a text file (`output.txt`).
- Easy to customize prompt and output settings.

---

## Requirements

- Python 3.6 or higher
- Anthropic API key
- Python packages:
  - `anthropic`

---

## Installation

1. Clone the repository:

```
git clone https://github.com/Julianhornero/ClaudeAI.git
cd ClaudeAI
```

2. Install dependencies:

```
pip install anthropic
```

3. Set your Anthropic API key as an environment variable:

```
export ANTHROPIC_API_KEY="your_api_key_here"
```

---

## Usage

Edit the script or run it directly to generate an article from a prompt.

Example:

```
python generate_article.py
```

By default, the script generates an article on the topic:

> "The impact of artificial intelligence on modern education"

and saves it as `output.txt`.

---

## Example Code Snippet

```
import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

def generate_article(prompt: str, output_file: str = "output.txt"):
    full_prompt = (
        f"{HUMAN_PROMPT} Write a detailed article about the following topic:\n\n"
        f"{prompt}\n\nArticle:{AI_PROMPT}"
    )
    response = client.completions.create(
        model="claude-3",
        prompt=full_prompt,
        max_tokens_to_sample=1000,
        stop_sequences=["\n\n"]
    )
    article = response.completion.strip()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(article)
    print(f"Article generated and saved to {output_file}")

if __name__ == "__main__":
    topic = "The impact of artificial intelligence on modern education"
    generate_article(topic)
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
