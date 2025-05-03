from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

class Hermes:
    def __init__(self):
        model_name = "facebook/blenderbot-3B"  # This is the large 3B model. You can also try "facebook/blenderbot-400M-distill" for a smaller one.
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

    def generate_response(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        output = self.model.generate(**inputs, max_length=max_length, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

# Example Usage:
hermes = Hermes()
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = hermes.generate_response(user_input)
    print("Hermes:", response)

