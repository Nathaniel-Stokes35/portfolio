from flask import Flask, request, jsonify, render_template
import re
import os

app = Flask(__name__)

def discover(desc, att): # Function to discover the nuance of the Storyboard for the adventure
    person_scores = [0, 0, 0, 0, 0, 0, 0, 0]  # E, I, N, S, F, T, P, J
    desc_weight = 0.7 # The description of how the player describes the character, outweighs the natural attribute pull
    att_weight = 0.3 # But it is still something that should be considered

    att_modifiers = {
    'intelligence': [-2, -2, -3, 1],   # ISTP
    'strength': [1, -2, -1, -1],       # ESTJ
    'endurance': [-1, -3, -2, 1],      # ISTP
    'charisma': [3, 2, 3, 1],          # ENFP
    'wisdom': [1, 2, 2, -1],           # ENFJ
    'agility': [-1, 2, 2, -1]          # INFJ  
    }

    E = ['outgoing','charismatic','bold','social','adventurous','energetic','talkative','expressive','leader','optimistic','enthusiastic','engaging','funloving','gregarious','assertive'] # Extrovert Words
    I = ['quiet','reflective','thoughtful','reserved','independent','observant','contemplative','private','mysterious','shy','introspective','calm','focused','selfsufficient','self','serene'] # Introvert Words

    N = ['imaginative','visionary','creative','abstract','theoretical','insightful','curious','innovative','future','idealistic','conceptual','dreamer','pattern','reflective', 'imagination', 'vision'] # Intuition Words
    S = ['practical','realistic','detail','observant','grounded','logical','concrete','present','action','reliable','precise','sensible','cautious','hands','focused', 'dirty', 'mess', 'clean', 'touch'] # Sensory Words

    F = ['compassionate','empathetic','caring','sensitive','altruistic','harmonious','supportive','kind','heart','idealistic','genuine','considerate','patient','warm','understanding','cooperative'] # Feeling Words
    T = ['Analytical','logical','objective','strategic','decisive','detached','independent','rational','problemsolver','solver','skeptical','critical','realistic','efficient','pragmatic','direct', 'smart'] # Thinking Words

    P = ['spontaneous','flexible','openminded','open','adaptable','curious','freespirited','free','playful','resourceful','creative','unconventional','disorganized','exploratory','risktaking','risk','innovative','carefree','careless'] # Prospecting Words
    J = ['organized','structured','responsible','decisive','planner','disciplined','systematic','goaloriented','goal','reliable','focused','efficient','methodical','conscientious','punctual','predictable'] # Judging Words

    # Apply attribute modifiers based on selected attributes (ENFP(+) ISTJ(-))
    for attribute in att:
        if attribute in att_modifiers:
            modifiers = att_modifiers[attribute]
            # Dampening the modification so the attributes are simply personality guideposts, but also to assign defaults if no description was made.
            
            # Extraversion (E) vs Introversion (I)
            person_scores[0] += modifiers[0] * 0.25  
            person_scores[1] -= modifiers[0] * 0.25  
            
            # Intuition (N) vs Sensing (S)
            person_scores[2] += modifiers[1] * 0.25 
            person_scores[3] -= modifiers[1] * 0.25  
            
            # Feeling (F) vs Thinking (T)
            person_scores[4] += modifiers[2] * 0.25  
            person_scores[5] -= modifiers[2] * 0.25 
            
            # Perceiving (P) vs Judging (J)
            person_scores[6] += modifiers[3] * 0.25  
            person_scores[7] -= modifiers[3] * 0.25  

    # Breaking down the user's character description word by word and associating predetermined words to personality traits for that character if they were used
    clean_desc = re.sub(r'[^\w\s]', '', desc) # Cleaning the description and leaving only words and whitespaces
    desc_words = clean_desc.split() # Seperating each word to run in the for loop to see if they match predefined words
    for word in desc_words:
        if word in E:
            person_scores[0] += 1
        if word in I:
            person_scores[1] += 1
        if word in N:
            person_scores[2] += 1
        if word in S:
            person_scores[3] += 1
        if word in F:
            person_scores[4] += 1
        if word in T:
            person_scores[5] += 1
        if word in P:
            person_scores[6] += 1
        if word in J:
            person_scores[7] += 1

    # Normalizing values and applying weights
    for i in range(8):
        person_scores[i] = person_scores[i] * desc_weight + person_scores[i] * att_weight

    # Determing the dominant traits for each pair (E/I, N/S, F/T, P/J) (If attributes are tied they default to ESFJ respectivly which is the most common trait in EACH of the 4 categories)
    e_i = "E" if person_scores[0] > person_scores[1] else "I"
    n_s = "S" if person_scores[3] > person_scores[2] else "N"
    f_t = "F" if person_scores[4] > person_scores[5] else "T"
    p_j = "J" if person_scores[7] > person_scores[6] else "P"

    MBTI = (e_i+n_s+f_t+p_j).upper()
    type = get_personality_name(MBTI)

    return [type[0], type[1], type[2]]

# Function: get_personality_name
def get_personality_name(MBTI):
    # Mapping for MBTI types to their personality name and gameplay impact description
    if MBTI == 'INTJ':
        return ['The Architect', (
            'Approach: Logical, strategic, prefers long-term solutions.\nGameplay Impact: Might approach negotiations with a meticulous, calculated strategy, opting for planned, methodical discussions.' + os.linesep +
            'These players would excel in situations requiring a clear, logical argument but might struggle in emotionally charged situations.' + os.linesep +
            'Possible Scenarios: "Negotiate the terms using hard data," "Create a strategic alliance for future gain," "Advocate for a systemized solution."')]
    if MBTI == 'INTP':
        return ['The Thinker', (
            'Approach: Inventive, curious, loves abstract ideas and theories.' + os.linesep +
            'Gameplay Impact: Likely to take a more unconventional approach in dialogue, proposing creative but perhaps impractical solutions. They may question authority and challenge the status quo, which could result in conflict or new opportunities.' + os.linesep +
            'Possible Choices: "Explore a theoretical solution to the issue," "Challenge assumptions and propose something radical," "Consider an alternative perspective."')]
    if MBTI == 'ENTJ':
        return ['The Commander', (
            'Approach: Assertive, determined, focused on results.' + os.linesep +
            'Gameplay Impact: Characters with this personality would have strong, forceful dialogue options, demanding respect and pushing for quick, decisive action. They may try to impose their will on situations and could face resistance or admiration depending on the outcome.' + os.linesep +
            'Possible Choices: "Take charge of the situation and dictate terms," "Leverage authority to bend the rules," "Take immediate action to secure a victory."')]
    if MBTI == 'ENTP':
        return ['The Debater', (
            'Approach: Outspoken, enjoys arguing and testing ideas.' + os.linesep +
            'Gameplay Impact: Known for being persuasive, they might engage in witty or sarcastic repartee during diplomatic situations. The Debator\'s could turn confrontations into debates, potentially winning allies through charm or sharp arguments.' + os.linesep +
            'Possible Choices: "Debate the other party into submission," "Challenge the opposing argument with logic," "Play devil\'s advocate to get more information."')]
    if MBTI == 'ISTJ':
        return ['The Logistician', ('Approach: Practical, dependable, values tradition.' + os.linesep +
            'Gameplay Impact: Logisticians will likely approach diplomatic situations with a strong sense of duty and an adherence to rules. They prefer clear, organized solutions and will avoid ambiguity.' + os.linesep +
            'Possible Choices: "Propose a tried-and-true solution," "Stick to tradition and established norms," "Offer a detailed, step-by-step plan."')]
    if MBTI == 'ISFJ':
        return ['The Defender', ('Approach: Loyal, supportive, focuses on security.' + os.linesep +
            'Gameplay Impact: Defenders are service-oriented, often putting others\' needs first. In a diplomatic context, they will likely mediate and support the needs of others rather than assert their own will.' + os.linesep +
            'Possible Choices: "Advocate for the protection of those who need help," "Ensure everyone\'s safety before proceeding," "Create a solution that preserves stability and order."')]
    if MBTI == 'ESTJ':
        return ['The Executive', ('Approach: Efficient, organized, prefers structure and authority.' + os.linesep +
            'Gameplay Impact: Executives are likely to be straightforward and practical, preferring decisive actions that are well-planned. They would excel in roles where they can take charge and lead with authority.' + os.linesep +
            'Possible Choices: "Make a decision and implement it immediately," "Organize the team to complete the task effectively," "Stick to a well-structured plan."')]
    if MBTI == 'ESFJ':
        return ['The Consul', ('Approach: Social, caring, values cooperation.' + os.linesep +
            'Gameplay Impact: Consuls are likely to seek cooperative, peaceful solutions, relying on their strong interpersonal skills. They may work to ensure everyone is happy and included, sometimes at the cost of more practical or idealistic goals.' + os.linesep +
            'Possible Choices: "Appeal to the group\'s sense of community," "Find a consensus that everyone can agree on," "Ensure that no one is left behind in the discussion."')]
    if MBTI == 'ISTP':
        return ['The Virtuoso', ('Approach: Analytical, flexible, enjoys hands-on problem solving.' + os.linesep +
            'Gameplay Impact: Virtuoso\'s are likely to approach diplomatic situations with pragmatism and flexibility, often looking for solutions based on action rather than words. They might favor direct solutions that require little negotiation.' + os.linesep +
            'Possible Choices: "Find a practical solution that requires action," "Use logic to simplify the situation," "Make quick decisions and adapt as things change."')]
    if MBTI == 'ISFP': 
        return ['The Adventurer', ('Approach: Artistic, gentle, values personal freedom.' + os.linesep +
            'Gameplay Impact: Adventurers would focus on harmonious, creative solutions to diplomacy, offering peaceful ways to resolve conflict. They may have a more emotional, heartfelt approach to negotiations.' + os.linesep +
            'Possible Choices: "Appeal to the emotions of others," "Use creativity to inspire a peaceful resolution," "Suggest a flexible, open-ended compromise."')]
    if MBTI == 'ESTP':
        return ['The Entrepreneur', ('Approach: Energetic, bold, enjoys excitement.' + os.linesep +
            'Gameplay Impact: Entrepreneurs are likely to engage with a bold, spontaneous approach. They thrive in action-oriented environments and may push for immediate solutions, sometimes foregoing diplomacy in favor of action.' + os.linesep +
            'Possible Choices: "Take action without waiting for consensus," "Challenge others to make a quick decision," "Push forward with a bold plan."')]
    if MBTI == 'ESFP':
        return ['The Entertainer', ('Approach: Fun-loving, spontaneous, enjoys the moment.' + os.linesep +
            'Gameplay Impact: Entertainers would likely use charismatic charm to win over others and create a fun, easygoing atmosphere. They may use humor and lightheartedness to diffuse tension, although they can command more serious confrontations.' + os.linesep +
            'Possible Choices: "Lighten the mood with humor," "Charm the group into agreeing with your idea," "Suggest a spontaneous, fun solution to the problem."')]

    return ['Unknown Personality', 'No description available.', MBTI]

# Function: class_check
def class_check(att, set):
    first_att, second_att = [attr.strip().lower() for attr in att]
    
    class_mapping = {
        'spa': {
            ('str', 'int'): {'class': 'shock-trooper', 'description': 'A powerful leader who excels in close combat and strategic planning.'},  # Leader
            ('str', 'agi'): {'class': 'tactician', 'description': 'A survivor who relies on agility and quick thinking to outmaneuver enemies.'},  # Survivor
            ('str', 'wis'): {'class': 'war-hero', 'description': 'A resourceful survivor with knowledge of tactics and survival skills.'},  # Diplomat
            ('str', 'cha'): {'class': 'smuggler', 'description': 'A charismatic diplomat who can talk their way out of almost any situation.'},  # Diplomat
            ('str', 'end'): {'class': 'survivalist', 'description': 'A hardy survivor focused on enduring the harshest environments.'},  # Survivor
            ('int', 'agi'): {'class': 'hacker', 'description': 'A tech-savvy individual who can manipulate systems and hack into networks.'},  # Tech
            ('int', 'wis'): {'class': 'doctor', 'description': 'A skilled medic who can heal wounds and treat ailments with precision.'},  # Tech
            ('int', 'cha'): {'class': 'embassy-diplomat', 'description': 'A charming negotiator who excels in diplomatic relations.'},  # Diplomat
            ('int', 'end'): {'class': 'researcher', 'description': 'A methodical and curious individual dedicated to discovering new technologies.'},  # Tech
            ('agi', 'wis'): {'class': 'stowaway', 'description': 'A stealthy individual who can blend into the background and avoid detection.'},  # Stealth
            ('agi', 'cha'): {'class': 'scoundrel', 'description': 'A charming and agile rogue who uses wit and cunning to outsmart their foes.'},  # Stealth
            ('agi', 'end'): {'class': 'scout', 'description': 'A quick and observant individual who excels at reconnaissance and exploration.'},  # Stealth
            ('wis', 'cha'): {'class': 'squad-leader', 'description': 'A seasoned leader who can command troops with wisdom and authority.'},  # Leader
            ('wis', 'end'): {'class': 'worker', 'description': 'A battle-hardened warrior who leads with courage and strength.'},  # Survivor
            ('cha', 'end'): {'class': 'commander', 'description': 'A charismatic and strategic leader, known for their decisive nature and tactical mind.'}  # Leader
        },
        'fan': {
            ('str', 'int'): {'class': 'battle mage', 'description': 'A mage who combines martial prowess with magical abilities for devastating results.'},  # Mage
            ('str', 'agi'): {'class': 'monk', 'description': 'A skilled fighter focused on hand-to-hand combat and quick strikes.'},  # Fighter
            ('str', 'wis'): {'class': 'fighter', 'description': 'A strong and resilient warrior, well-versed in a variety of combat styles.'},  # Fighter
            ('str', 'cha'): {'class': 'warlord', 'description': 'A powerful and charismatic guardian who leads their people with might and wisdom.'},  # Guardian
            ('str', 'end'): {'class': 'barbarian', 'description': 'A fierce and untamed warrior who relies on strength and endurance.'},  # Fighter
            ('int', 'agi'): {'class': 'rogue', 'description': 'A stealthy character who specializes in subterfuge, stealth, and surprise attacks.'},  # Stealth
            ('int', 'wis'): {'class': 'shaman', 'description': 'A spiritual and wise nature-based caster who can commune with the elements.'},  # Nature
            ('int', 'cha'): {'class': 'spy', 'description': 'A covert agent skilled in espionage and gathering vital information.'},  # Stealth
            ('int', 'end'): {'class': 'healer', 'description': 'A dedicated mage focused on healing and supporting allies in battle.'},  # Mage
            ('agi', 'wis'): {'class': 'thief', 'description': 'A nimble and quick character who specializes in stealth and stealing valuable items.'},  # Stealth
            ('agi', 'cha'): {'class': 'beastmaster', 'description': 'A master of animals, using their bond with creatures to gain an advantage in combat.'},  # Nature
            ('agi', 'end'): {'class': 'ranger', 'description': 'A guardian skilled in ranged combat and survival in the wild.'},  # Guardian
            ('wis', 'cha'): {'class': 'cleric', 'description': 'A holy mage focused on healing and supporting allies through divine magic.'},  # Mage
            ('wis', 'end'): {'class': 'druid', 'description': 'A nature-based caster who can shapeshift and command the forces of nature.'},  # Nature
            ('cha', 'end'): {'class': 'paladin', 'description': 'A noble and righteous warrior who fights for justice and the protection of others.'}  # Guardian
        },
        'pir': {
            ('str', 'int'): {'class': 'corsair', 'description': 'An imperial pirate with a mastery of naval combat and swashbuckling.'},  # Imperial
            ('str', 'agi'): {'class': 'specialist', 'description': 'A versatile pirate skilled in various forms of combat and tactics.'},  # Trader
            ('str', 'wis'): {'class': 'captain', 'description': 'A seasoned leader who commands a pirate crew with experience and wisdom.'},  # Captain
            ('str', 'cha'): {'class': 'first-mate', 'description': 'A charismatic and reliable second-in-command aboard a pirate ship.'},  # Captain
            ('str', 'end'): {'class': 'bouncer', 'description': 'A strong and tough pirate who handles physical confrontations with ease.'},  # Swashbuckler
            ('int', 'agi'): {'class': 'swindler', 'description': 'A cunning and agile pirate who uses deception and trickery to outwit opponents.'},  # Trader
            ('int', 'wis'): {'class': 'alchemist', 'description': 'A pirate with knowledge of arcane potions and chemicals, useful in combat and healing.'},  # Arcana
            ('int', 'cha'): {'class': 'privateer', 'description': 'A pirate who operates with a sense of honor, often working for the crown.'},  # Imperial
            ('int', 'end'): {'class': 'quartermaster', 'description': 'A pirate in charge of supplies and inventory, ensuring the crew is well-equipped.'},  # Trader
            ('agi', 'wis'): {'class': 'navigator', 'description': 'A skilled sailor and mapmaker, essential for navigating the high seas.'},  # Imperial
            ('agi', 'cha'): {'class': 'swashbuckler', 'description': 'A daring and charming pirate who excels in close combat with a rapier.'},  # Swashbuckler
            ('agi', 'end'): {'class': 'deckhand', 'description': 'A hardworking pirate who performs essential tasks aboard a ship.'},  # Swashbuckler
            ('wis', 'cha'): {'class': 'witchdoctor', 'description': 'A mystical pirate who uses dark magic and potions to heal and curse others.'},  # Arcana
            ('wis', 'end'): {'class': 'medic', 'description': 'A pirate healer who uses knowledge of anatomy and medicine to tend to injuries.'},  # Arcana
            ('cha', 'end'): {'class': 'pirate lord', 'description': 'A powerful and influential pirate captain, ruling over the high seas.'}  # Captain
        }
    }

    if (first_att[:3], second_att[:3]) in class_mapping[set]:
        return class_mapping[set][(first_att[:3], second_att[:3])]
    elif (second_att[:3], first_att[:3]) in class_mapping[set]:  # Handle reverse order of attributes
        return class_mapping[set][(second_att[:3], first_att[:3])]
    else:
        return {"class": "Unknown", "description": "No class found for these attributes."}

# Route to display the main page (for character creation or personality quiz)
@app.route('/')
def index():
    return render_template('personal.html')

@app.route('/get_class', methods=['POST'])
def get_class():
    # Get the selected attributes from the request body
    data = request.get_json()
    selected_attributes = data.get('attributes', [])
    selected_set = data.get('set', 'spa')
    
    # Call the function to determine the class title
    result = class_check(selected_attributes, selected_set)

    class_name = result.get('class', 'Unknown')
    description = result.get('description', 'No description available')
    
    # Return the class name as JSON
    return jsonify({'className': class_name, 'description':description})

@app.route('/create_character', methods=['POST'])
def create_character():
    # Get the description and attributes from the form
    character_desc = request.form['character_desc']
    attributes = request.form.getlist('attributes')
    theme = request.form['theme']

    # Discover personality based on description and attributes
    personality_name, personality_description, MBTI = discover(character_desc, attributes)

    # Now, we can determine the class based on attributes and theme
    character_class = class_check(attributes, theme)

    return jsonify({
        'personality': {
            'name': personality_name,
            'description': personality_description
        },
        'character_class': character_class
    })

if __name__ == '__main__':
    app.run(debug=True)