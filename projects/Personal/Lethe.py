import random
import numpy as np
from transformers import BertTokenizer
from transformers import GPT2Tokenizer
from transformers import GPT2LMHeadModel
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from collections import deque

# The "Survival" Model (Simple Linear Regression-like behavior)
class SurvivalModel:
    def __init__(self):
        self.needs = ['food', 'safety', 'comfort'] 
        self.priority = {need: random.random() for need in self.needs}
    
    def prioritize(self):
        return sorted(self.priority.items(), key=lambda x: x[1], reverse=True)

# The "Conscious" Model (Complex Decision-Making)
class ConsciousModel:
    def __init__(self):
        self.objectives = ['long-term goals', 'social dynamics', 'emotional intelligence']
        self.priority = {objective: random.random() for objective in self.objectives}
    
    def prioritize(self):
        return sorted(self.priority.items(), key=lambda x: x[1], reverse=True)

# The "Higher Learning" Model (Self-Actualization)
class HigherLearningModel:
        
    """This model will have to govern the other two in a powerful, meaningful, organized way.
        This model will prioritize decisions with the survival being the only model that can override under extreme conditions.
        This model will assign priority and needs based on the 'Higher Law'"""

    def __init__(self):
        self.values = ['growth', 'philosophy', 'abstract thought']
        self.priority = {value: random.random() for value in self.values}
    
    def prioritize(self):
        return sorted(self.priority.items(), key=lambda x: x[1], reverse=True)

# Memory Management (For storing and condensing memories)
class Memory:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = []

    def add_short_term_memory(self, memory):
        self.short_term_memory.append(memory)
    
    def condense_memory(self):
        # Simplified condensing logic for now
        self.long_term_memory = self.short_term_memory[-5:]  # Keeping the last 5 memories
    
    def get_long_term_memory(self):
        return self.long_term_memory

# Assistant Model
class Lethe:
    def __init__(self, name="Hermes"):
        self.name = name
        self.survival_model = SurvivalModel()
        self.conscious_model = ConsciousModel()
        self.higher_learning_model = HigherLearningModel()
        self.memory = Memory()

    def introduce(self):
        print(f"Hello, I am {self.name}. How can I assist you today?")
        
    def train(self, age, history, personality):
        print(f"Training model with age: {age}, history: {history}, personality: {personality}")

        # Simulate training by adjusting priorities based on the input
        tokenizer_lower = BertTokenizer.from_pretrained('bert-base-uncased')
        text = "I went to Walmart and bought milk, butter, and eggs."
        encoded_text = tokenizer_lower.encode(text, add_special_tokens=True)
        print(f"Tokenized (WordPiece) text: {encoded_text}")
        
        # Load pre-trained GPT-2 tokenizer
        tokenizer_higher = GPT2Tokenizer.from_pretrained('gpt2')
        text = "I feel happy today because it's my birthday."
        encoded_text = tokenizer_higher.encode(text, add_special_tokens=True)
        print(f"Tokenized (GPT-2) text: {encoded_text}")

        self.survival_model.priority['food'] += random.random() * 0.2
        self.conscious_model.priority['long-term goals'] += random.random() * 0.2
        self.higher_learning_model.priority['growth'] += random.random() * 0.2
        
    def interact(self):
        print("Let's have a conversation!")
        # Here we can allow for more dynamic interaction logic
        response = random.choice([
            "How are you feeling today?",
            "What's on your mind?",
            "What goals do you have today?"
        ])
        print(f"{self.name}: {response}")

    def recall_memory(self):
        print(f"{self.name} recalls memory: {self.memory.get_long_term_memory()}")

class MemoryManager:
    def __init__(self):
        self.memory = deque(maxlen=100)  # Limit the memory size
        self.condensed_memory = []

    def add_memory(self, text, tokenizer, level):
        """Add a memory based on model level (lower or higher-level)."""
        if level == 'lower':
            tokens = tokenizer.encode(text, add_special_tokens=True)
            vector = np.mean(tokens)  # A simple method to condense tokens (mean for simplicity)
        else:
            # For higher level models (GPT-2/3), use sentence embeddings or token vectors
            tokens = tokenizer.encode(text, add_special_tokens=True)
            vector = np.mean(tokens)  # Adjust based on better vectorization techniques (e.g., embeddings)
        
        self.memory.append(tokens)  # Store raw memory
        self.condense_memory(vector)  # Condense memory

    def condense_memory(self, vector):
        """Condense the memory vectors over time to reduce complexity."""
        self.condensed_memory.append(vector)  # You can optimize this step further with a more advanced approach
        if len(self.condensed_memory) > 50:
            self.condensed_memory = self.condensed_memory[-50:]  # Keep the last 50 condensed memories
    
    def get_memory(self):
        """Return current raw and condensed memory."""
        return list(self.memory), list(self.condensed_memory)

# Example usage
memory_manager = MemoryManager()

tokenizer_lower = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer_higher = GPT2Tokenizer.from_pretrained('gpt2')

memory_manager.add_memory("I went to the store and bought some eggs.", tokenizer_lower, 'lower')
memory_manager.add_memory("The sun is shining today.", tokenizer_higher, 'higher')

model = GPT2LMHeadModel.from_pretrained('gpt2')

# Convert the condensed memory back into a string (for example purposes)
conversation_history = "I went to the store and bought some eggs."
input_ids = tokenizer_higher.encode(conversation_history, return_tensors='pt')

# Generate a response based on memory and previous interaction
output = model.generate(input_ids, max_length=50, num_return_sequences=1)
response = tokenizer_higher.decode(output[0], skip_special_tokens=True)

print("Model Response:", response)

print("Condensed Memory:", memory_manager.get_memory())

class AdvancedMemoryManager:
    def __init__(self):
        self.memory = deque(maxlen=100)  # Limit memory size
        self.embeddings = []
        self.memory_size = 50  # Number of clusters to keep

    def add_memory(self, text):
        """Generate sentence embedding and store in memory."""

        embedding = tokenizer_higher.encode(text, add_special_tokens=True)
        self.embeddings.append(embedding)
        self.memory.append(text)

        # Perform clustering and PCA when memory exceeds certain size
        if len(self.embeddings) > self.memory_size:
            self.condense_memory()

    def condense_memory(self):
        """Perform clustering and PCA on embeddings."""
        # Convert embeddings to a 2D array for clustering
        embeddings = np.vstack(self.embeddings)

        # Apply PCA to reduce dimensionality (e.g., to 100 dimensions)
        pca = PCA(n_components=100)
        reduced_embeddings = pca.fit_transform(embeddings)

        # Apply K-means clustering
        kmeans = KMeans(n_clusters=self.memory_size)
        kmeans.fit(reduced_embeddings)

        # For each cluster, store the representative memory (centroid)
        cluster_centroids = kmeans.cluster_centers_
        cluster_assignments = kmeans.predict(reduced_embeddings)

        condensed_memory = []
        for cluster_idx in range(self.memory_size):
            cluster_indices = np.where(cluster_assignments == cluster_idx)[0]
            cluster_texts = [self.memory[i] for i in cluster_indices]
            representative_text = self.get_representative_memory(cluster_texts)
            condensed_memory.append(representative_text)

        self.memory = deque(condensed_memory, maxlen=self.memory_size)
        self.embeddings = []

    def get_representative_memory(self, cluster_texts):
        """Choose the most representative memory for a cluster."""
        # For simplicity, take the first text as the representative
        return cluster_texts[0]

    def get_memory(self):
        """Return the condensed memory."""
        return list(self.memory)


# Example usage:
memory_manager = AdvancedMemoryManager()

memory_manager.add_memory("I went to the store and bought some eggs.")
memory_manager.add_memory("The sun is shining today.")
memory_manager.add_memory("I had a conversation with my friend about philosophy.")

# Add more memories
for i in range(20):
    memory_manager.add_memory(f"Random memory {i}")

# Get the condensed memory
print("Condensed Memory:", memory_manager.get_memory())

# Main Flow
def main():
    print("Welcome to Lethe Engine.")
    
    # Ask the user for the type of model they want
    age = input("What age would you like the model to be? ")
    history = input("What is the model's background? ")
    personality = input("What personality traits should the model have? ")
    
    # Create the assistant model
    assistant = Lethe()
    
    # Train the model
    assistant.train(age, history, personality)
    
    # Start interaction
    assistant.introduce()
    
    # Simulate memory logging
    assistant.memory.add_short_term_memory("Visited Walmart, bought Milk, Butter, and Eggs.")
    assistant.memory.add_short_term_memory("Had a conversation with the cashier.")
    
    assistant.memory.condense_memory()  # Condense memory
    assistant.recall_memory()  # Show long-term memory
    
    # Let assistant initiate conversation
    assistant.interact()

if __name__ == "__main__":
    main()