import os
import openai

# Load API key from environment or config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
openai.api_key = OPENAI_API_KEY

def classify_intent(message_text):
    """Placeholder function to classify patient message intent using OpenAI API"""
    prompt = f"Classify the intent of the patient message:\n\nMessage: {message_text}\n\nReturn: appointment / question / refill / billing / other"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        intent = response.choices[0].text.strip()
        return intent
    except Exception as e:
        print("Error calling OpenAI API:", e)
        return "unknown"

# Example usage
if __name__ == "__main__":
    sample_message = "I need to schedule a checkup next week"
    print("Predicted intent:", classify_intent(sample_message))
