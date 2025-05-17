import { writeFileSync } from 'fs';
import { Anthropic } from '@anthropic-ai/sdk';

// Initialize the Anthropic client with your API key
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY, // Set your API key in environment variables
});

async function generateArticle(prompt) {
  try {
    // Create a completion request to Claude
    const response = await anthropic.completions.create({
      model: 'claude-3', // or 'claude-3-7-sonnet-20250219' or latest available
      prompt: `Write a detailed article about the following topic:\n\n${prompt}\n\nArticle:`,
      max_tokens_to_sample: 1000, // adjust as needed
      stop_sequences: ['\n\n'], // stop after the article
    });

    const article = response.completion.trim();

    // Save the article to output.txt
    writeFileSync('output.txt', article, 'utf-8');
    console.log('Article generated and saved to output.txt');
  } catch (error) {
    console.error('Error generating article:', error);
  }
}

// Example usage
const topic = "The impact of artificial intelligence on modern education";
generateArticle(topic);
