import random
import time
import torch
import numpy as np
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import pipeline
from catboost import CatBoostClassifier

class SentimentAnalysis:
    def __init__(self):
        # Initialize a sentiment analysis pipeline using Hugging Face
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the text (positive, negative, or neutral).
        Returns a sentiment score and label.
        """
        result = self.sentiment_analyzer(text)[0]
        sentiment = result['label']
        score = result['score']
        return sentiment, score


class SimpleAgent:
    def __init__(self, name="Hermes", emotional_state=5, description="a constructive AI helper", threshold=-0.5):
        self.name = name
        self.emotional_state = emotional_state
        self.description = description
        self.threshold = threshold  # Threshold for sentiment analysis
        self.self_identity = f"I am {self.name}, {self.description}."
        self.memory = []  # A simple list to store recent events
        
        # Load BlenderBot (distilled version) for dialogue generation
        self.tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        self.model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        # Load the sentiment analysis module
        self.sentiment_analyzer = SentimentAnalysis()
        
        # Initialize CatBoost model (assuming it's already trained)
        self.catboost_model = CatBoostClassifier()

    def add_memory(self, text):
        """Append a new memory; limit the memory list to the last 10 events."""
        self.memory.append(text)
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]

    def reflect(self):
        """
        Update self-identity based on the number of experiences and current emotional state.
        """
        reflection = f"I have experienced {len(self.memory)} events, and my emotional state is {self.emotional_state}."
        self.self_identity = reflection
        return self.self_identity

    def check_survival_threshold(self, sentiment_score):
        """
        Check if the sentiment score falls below the threshold.
        If it does, return a warning or special handling message.
        """
        if sentiment_score < self.threshold:
            return True
        return False

    def classify_input(self, user_input):
        """
        Classify the input using the CatBoost model (for intent recognition).
        """
        # Prepare the input for the CatBoost model (you would vectorize it)
        input_vector = np.array([user_input])  # Adjust this as per your CatBoost model's input format
        prediction = self.catboost_model.predict(input_vector)
        return prediction[0]  # Returning the predicted intent

    def generate_dialogue(self, user_input):
        """
        Generate a dialogue response using BlenderBot.
        The prompt includes the agent's current identity and a few recent memory events.
        """
        # Sentiment analysis of the user input
        sentiment, sentiment_score = self.sentiment_analyzer.analyze_sentiment(user_input)
        
        # If sentiment is below threshold, handle with caution or trigger support
        if self.check_survival_threshold(sentiment_score):
            response = "I'm really sorry to hear you're feeling this way. Can I help in some way?"
            self.add_memory(f"User: {user_input}")
            self.add_memory(f"{self.name}: {response}")
            return response

        # Classify the user input to determine intent
        intent = self.classify_input(user_input)
        print("DEBUG: Intent classified as:", intent)

        # Build a simple context: identity and up to the last three memories.
        recent_memories = "; ".join(self.memory[-3:]) if self.memory else "None"
        context = f"Identity: {self.self_identity}\nRecent memories: {recent_memories}\n"
        prompt = context + f"User: {user_input}\n{self.name}:"

        # Tokenize the prompt (with truncation to avoid overly long sequences)
        inputs = self.tokenizer([prompt], return_tensors="pt", truncation=True, max_length=512)
        if inputs["input_ids"].shape[1] == 0:
            return "I'm not sure what you mean. Could you rephrase that?"
        
        # Move inputs to the correct device
        inputs = {key: val.to(self.device) for key, val in inputs.items()}

        try:
            outputs = self.model.generate(
                inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=150,  # Limit the generated sequence length
                num_beams=5,
                early_stopping=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
            if outputs is None or outputs.size(0) == 0 or outputs.size(1) == 0:
                response = "I'm having trouble processing that right now. Could you try again?"
            else:
                response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print("Error during generation:", e)
            response = "I'm having trouble processing that right now. Could you try again?"

        # Save the interaction as memory events
        self.add_memory(f"User: {user_input}")
        self.add_memory(f"{self.name}: {response}")
        return response

def main():
    # Create the agent with a baseline emotional state and description.
    agent = SimpleAgent(name="Hermes", emotional_state=5, description="a constructive AI helper")
    print("Welcome! I am", agent.name)
    print("Type your messages below. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"{agent.name}: Goodbye! Talk to you later.")
            break

        # Generate and print the dialogue response.
        response = agent.generate_dialogue(user_input)
        print(f"{agent.name}: {response}")

        # Occasionally, let the agent reflect on its experiences.
        if random.random() < 0.3:
            print("Reflection:", agent.reflect())

if __name__ == "__main__":
    main()