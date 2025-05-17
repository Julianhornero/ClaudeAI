import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Initialize the Anthropic client with your API key
api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

def generate_article(prompt: str, output_file: str = "output.txt"):
    try:
        # Construct the prompt for Claude
        full_prompt = (
            f"{HUMAN_PROMPT} Write a detailed article about the following topic:\n\n"
            f"{prompt}\n\nArticle:{AI_PROMPT}"
        )

        response = client.completions.create(
            model="claude-3",  # or other available Claude models
            prompt=full_prompt,
            max_tokens_to_sample=1000,
            stop_sequences=["\n\n"]
        )

        article = response.completion.strip()

        # Save the article to output.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(article)

        print(f"Article generated and saved to {output_file}")

    except Exception as e:
        print(f"Error generating article: {e}")

if __name__ == "__main__":
    topic = "The impact of artificial intelligence on modern education"
    generate_article(topic)
