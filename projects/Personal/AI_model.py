import random

core_ideals = {
    "justice": 0.8,  # High emphasis on justice
    "loyalty": 0.6,  # Moderate loyalty
    "survival": 0.4, # Low survival instinct
    "freedom": 0.7   # High value on personal freedom
}

# Urgency Formula:
def calculate_priority_index(character, event):
    time_element = character.base - (event.time_passed * character.time_weight.get(event.category, 1))
    emotion_element = character.base - (event.intensity * character.emotion_weight.get(event.emotion, 1))

    time_index = round(time_element * 100)
    emotion_index = round(emotion_element * 100)

    return min(time_index, emotion_index)

def calculate_prompt_capacity(character, time_available):
    motivation_factor = character.motivation_level / 10  # Assuming motivation level is 1-10
    time_factor = time_available / 60  # Time available in minutes, normalized (e.g., 60 minutes = 1)
    
    # X is the number of prompts the AI can handle, which is influenced by both factors
    capacity = round(motivation_factor * time_factor * character.max_prompts)
    
    return max(1, capacity) 

# Example AI memory structure
memory_bank = {
    "memories": []
}

# Function to capture an event
def capture_event(event_details, core_ideals, memory_bank):
    # Define the event summary
    key_phrase = event_details['key_phrase']
    
    # Create an emotional base for the event
    base_emotion = event_details['emotion']
    emotion_intensity = event_details['intensity']

    # Calculate resonance (how strongly the event matches the AI's core ideals)
    resonance_score = calculate_resonance(event_details, core_ideals)
    emotional_response = apply_resonance(base_emotion, emotion_intensity, resonance_score)
    
    # Create memory entry
    new_memory = {
        "id": len(memory_bank['memories']) + 1,
        "key_phrase": key_phrase,
        "emotions": emotional_response,
        "timestamp": event_details['timestamp'],
        "event_details": event_details
    }
    
    # Add to the AI's memory bank
    memory_bank['memories'].append(new_memory)

    # Return updated memory bank
    return memory_bank

def decay_memory(memory, current_timestamp):
    memory_age = (current_timestamp - memory['timestamp']).total_seconds()
    decay_factor = max(0, 1 - memory_age / (60 * 60 * 24 * 30))  # Decay over 30 days
    memory['emotions'][0]['intensity'] *= decay_factor
    return memory

# Function to calculate resonance score
def calculate_resonance(event_details, core_ideals):
    # Check how much the event aligns with AI's core ideals
    resonance_score = 0
    for ideal, intensity in core_ideals.items():
        if ideal in event_details['key_phrase'].lower():
            resonance_score += intensity
    
    # Normalize resonance score (you can adjust this logic)
    resonance_score = min(resonance_score, 1.0)
    return resonance_score

# Function to apply the resonance and modify emotional intensity
def apply_resonance(base_emotion, intensity, resonance_score):
    # Apply the resonance score to the emotional intensity
    new_intensity = intensity * (1 + resonance_score)  # Amplify intensity based on resonance
    
    # Add the emotional context
    emotional_response = [{
        "emotion": base_emotion,
        "intensity": round(new_intensity, 2),
        "context": f"This event feels {base_emotion} due to its connection with my core beliefs."
    }]
    
    return emotional_response

# Example event to capture
event = {
    'key_phrase': "I betrayed my comrades to protect the innocent.",
    'emotion': "guilt",
    'intensity': 0.7,
    'timestamp': "2025-01-08T12:00:00Z"
}

# Capture the event
updated_memory_bank = capture_event(event, core_ideals, memory_bank)

# Display updated memory bank
print(updated_memory_bank)