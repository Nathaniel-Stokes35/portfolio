var character_data = {
    att: {
        strength : 0,
        intelligence : 0,
        endurance : 0,
        charisma : 0,
        wisdom : 0,
        agility : 0,
        e : 0,
        i : 0,
        n : 0,
        s : 0,
        f : 0,
        t : 0,
        p : 0,
        j : 0
    }
};
var selectedAttributes = [];
var sortedAttributes = [];
var selected = [];
var selectedSet = "";
var selected_class = "";
var personality = [];

var curr_question = 0;
var app_questions = [
    {
        question : "Your friend presents you with a complicated puzzle on the bus, that you've never seen before. The puzzle is interesting and your friend seems excited to have you try.", 
        options : [
            { text: "Study the puzzle attempting new ways to approach the problems it presents, not putting it down until it's solved.", attributes: "intelligence,1,endurance,1"},
            { text: "Chuckle at the notion he'd assume you would care. Snap the puzzle in two and hand it back to him still chuckling as you walk away.", attributes: "intelligence,-1,strength,1"},
            { text: "Study the puzzle briefly, weighing whether you can solve it. Looking around you see a kid sitting behind you, you turn and dare him to solve it.", attributes: "intelligence,1,charisma,1"},
            { text: "Watch your friend's reaction to the different ways you handle the puzzle, trying to find a clue as to how it's solved.", attributes: "intelligence,1,wisdom,1"},
            { text: "Analyzing the puzzle, you notice how the pieces move together, knowing if you're quick enough with your movements you can bypass a major segement of the puzzle alltogether.", attributes: "intelligence,1,agility,1"}
        ]},
    {
        question : "You're participating in an athletic competition when you see someone you like watching you, wanting to impress them you...", 
        options : [
            { text: "Find the heaviest peice of equipment hoping to hoist it over your shoulder and showing them how much you can handle.", attributes: "strength,1,endurance,1"},
            { text: "You quickly analyze and preform what would provide the most \"awe\" that you can safely do without too much effort.", attributes: "strength,-1,intelligence,1"},
            { text: "Give them a wink as you flex, then a soft smile as you complete your menuvear in the flashiest of ways.", attributes: "strength,1,charisma,1"},
            { text: "Remember what they said to you about what they enjoyed in your practice, Begin to show them the results of your training.", attributes: "strength,1,wisdom,1"},
            { text: "Hoping to show off, you quickly assess the best way to move through the competition, relying on your strength and quick movements to impress them with your speed.", attributes: "strength,1,agility,1"}
        ]},
    {
        question : "You've found yourself stranded and lost in some dark woods, whether you came here intentionally or by accident doesn't matter, what do you do?", 
        options : [
            { text: "Keep moving forward, pushing through exhaustion and fear, determined to find a way out no matter how long it takes.", attributes: "endurance,1,strength,1"}, 
            { text: "Start by finding shelter and food, preparing to endure the night with what little resources you have.", attributes: "endurance,1,wisdom,1"}, 
            { text: "Sit down and try to focus, conserving your energy while thinking of the best way to escape or survive.", attributes: "endurance,1,intelligence,1"}, 
            { text: "Shout for help, hoping that someone can hear you, continuing to look for an exit but beginning to get worried about how much longer you can make it alone.", attributes: "endurance,-1,charisma,1"}, 
            { text: "Start walking in a specific direction, hoping to find a way out, focusing on staying calm and pushing through.", attributes: "endurance,1,agility,1"}
        ]},
    {
        question : "You are at a friends party and the games are about to start but you notice your friend doesn't seem all that interested, so you ...", 
        options : [
            { text: "Walk over to your friend, put your arm around them, and pull them towards the group with a playful but firm challenge and invitation.", attributes: "charisma,1,strength,1"}, 
            { text: "You come up with an exciting and interesting new way to play the game hoping it will arouse their curiosity.", attributes: "charisma,1,intelligence,1"}, 
            { text: "Calmly walk over and engage in a heart to heart, trying to understand what might be throwing them off and listening to what they have to say.", attributes: "charisma,1,wisdom,1"}, 
            { text: "Comically waddle over to them trying your best to make them laugh. Acting Loud you demand the game move to the pair of you; hoping to get them involved with your lively energy.", attributes: "charisma,1,agility,1"}, 
            { text: "Ignoring them you continue to have fun at the party, you won't let their bad mood spoil your fun.", attributes: "charisma,-1,endurance,1"}
        ]},
    {
        question : "You come across a difficult scene after a hard day of work, it looks like some children have encountered the neighborhood cat dead in the allyway next to your home. You decide to... ", 
        options : [
            { text: "Take a deep breath, crouch down, and calmly explain to the children what has happened, offering them reassurance and suggesting they leave the area to play and get their minds off of it.", attributes: "wisdom,1,charisma,1"}, 
            { text: "Pause for a moment, reflecting on how to best help the children process their feelings, then you gently lead them away from the scene, offering a quiet, comforting presence.", attributes: "wisdom,1,endurance,1"}, 
            { text: "Call animal control, keeping the children safe and out of harm's way, while ensuring proper steps are taken to not attract more wildlife.", attributes: "wisdom,-1,intelligence,1"}, 
            { text: "say nothing to the children, not wanting to disturb their innocence. With a heavy heart you simply gather the cat and move it away, not making eye-contact or acknowledging any of the children.", attributes: "wisdom,1,strength,1"}, 
            { text: "Assess the situation thoughtfully, then offer to guide the children through a ritual of saying goodbye to the cat, helping them understand the natural cycle of life and death.", attributes: "wisdom,1,agility,1"}
        ]},
    {
        question : "You don't know how you ended up here but, looking at the barrel of a loaded .357 magnum, you hold your hands over your head offering vulnerability to the angry table player and... ", 
        options : [
            { text: "Slowly and carefully, you reach for the chair behind you, using it to carefully maneuver the chair until you can quickly and decisively throw it at the assaliant.", attributes: "agility,1,strength,1"},
            { text: "You drop to the floor, quickly rolling behind the counter saying \"Now I thought this was going to be a friendly game!\".", attributes: "agility,1,charisma,1"},
            { text: "With a deep breath, you sit back down at the table, moving your hands slowly and deliberately on the table, resting against the scattered chips, hoping to avoid further provocation.", attributes: "agility,-1,wisdom,1"},
            { text: "You steady yourself, then with a surge of perserverance, you push the table aside, fighting to close the gap and grab his gun.", attributes: "agility,1,endurance,1"},
            { text: "You calculate the best way to dodge or disarm the opponent, your mind racing through potential outcomes as you plan your next move.", attributes: "agility,1,intelligence,1"}
        ]},
    {
        question : "You find yourself in a large group of strangers, no one seems to know what's going on or why they're here. What do you do?",
        options : [
            { text: "I need to find out what's going on. You look around for anything out of the ordinary that stands out, people, things, doesn't matter... What doesn't belong?", attributes: "i,1,s,1"},
            { text: "Engage with the people around you, was there something you missed?", attributes: "e,1,n,1"},
            { text: "Punch the person next to you, might as well make this exciting.", attributes: "e,0,j,2"},
            { text: "Start telling people you'll let them leave if they pay you $10.", attributes: "e,1,j,1"},
            { text: "Check your pockets for any clues, do a quick survey of yourself to understand what kind of condition you are in.", attributes: "i,1,f,1"}
        ]},
    { 
        question : "You've made a wrong turn heading to your mothers house. Looking around you see a few paths laid before you. You choose to...", 
        options : [
            { text: "try and recall the time you went to your mom's house, closing your eyes to mentally recreate the directions you took", attributes: "n,1,t,1"},
            { text: "Look around trying to find a possible landmark or something familiar that can help you get back on track.", attributes: "s,1,j,1"},
            { text: "Look around and knock on a door, seeing if you can be given directions. It's Practical but could be dangerous, if you knock on the wrong door.", attributes: "s,0,e,1"},
            { text: "Follow the path you were walking down earlier. After all, you *must* have been going in the right direction at the start.", attributes: "n,1,j,1"},
            { text: "Pull out your map and try to figure out where you are and where you need to be.", attributes: "s,1,t,1"}
        ]},
    {
        question : "Oh no! You've been exposed to radiation, and a mutated hand has grown out of your stomach. What is the best course of treatment?",
        options : [
            { text: "A bullet to the brain.", attributes: "f,2,j,2"},
            { text: "A large dose of anti-mutagen agent.", attributes: "f,1,s,1"},
            { text: "Prayer. Maybe God will spare you in exchange for a life of pious devotion.", attributes: "f,0,p,1"},
            { text: "Removal of the mutated tissue with a precision laser.", attributes: "t,1,s,1"},
            { text: "Observe, with a third hand you'll be able to complete tasks much faster.", attributes: "t,1,p,2"}
        ]},
    {
        question : "There is work that needs to be done and everyone else is laying around. What do you do?",
        options : [
            { text: "Lounge with them, if it's a group effort we can't all get in trouble.", attributes: "p,1,e,1"},
            { text: "Watch and wait for everyone else to get motivated, they know the work needs to be completed as much as you do.", attributes: "p,1,s,1"},
            { text: "Talk with a friend, maybe you can motivate him and together you can get the group working.", attributes: "j,0,t,1"},
            { text: "Grab a nearby pan and wooden spoon, walk around everyone banging the pan with the spoon and telling everyone to get up.", attributes: "j,1,e,1"},
            { text: "Explode a firecracker in a barrel next to one of your coworkers right before they doze off.", attributes: "j,1,t,1"}
        ]}
];
function title(word) {
    var words = word.split(' ');
    for (let i = 0; i < words.length; i += 1) {
        if (i === 0 || !['of', 'a', 'the'].includes(words[i].toLowerCase())) {
            words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1).toLowerCase();
        } else {
            words[i] = words[i].toLowerCase();
        }
    }
    return words.join(' ')
}
function class_check(att, set) {
    let [first_att, second_att] = att.slice(0, 2)

    const class_mapping = {
        'spa': {
            'str-int': { 'class': 'shock-trooper', 'description': 'A powerful leader who excels in close combat and strategic planning.' },
            'str-agi': { 'class': 'tactician', 'description': 'A survivor who relies on agility and quick thinking to outmaneuver enemies.' },
            'str-wis': { 'class': 'war-hero', 'description': 'A resourceful survivor with knowledge of tactics and survival skills.' },
            'str-cha': { 'class': 'smuggler', 'description': 'A charismatic diplomat who can talk their way out of almost any situation.' },
            'str-end': { 'class': 'survivalist', 'description': 'A hardy survivor focused on enduring the harshest environments.' },
            'int-agi': { 'class': 'hacker', 'description': 'A tech-savvy individual who can manipulate systems and hack into networks.' },
            'int-wis': { 'class': 'doctor', 'description': 'A skilled medic who can heal wounds and treat ailments with precision.' },
            'int-cha': { 'class': 'embassy-diplomat', 'description': 'A charming negotiator who excels in diplomatic relations.' },
            'int-end': { 'class': 'researcher', 'description': 'A methodical and curious individual dedicated to discovering new technologies.' },
            'agi-wis': { 'class': 'stowaway', 'description': 'A stealthy individual who can blend into the background and avoid detection.' },
            'agi-cha': { 'class': 'scoundrel', 'description': 'A charming and agile rogue who uses wit and cunning to outsmart their foes.' },
            'agi-end': { 'class': 'scout', 'description': 'A quick and observant individual who excels at reconnaissance and exploration.' },
            'wis-cha': { 'class': 'squad-leader', 'description': 'A seasoned leader who can command troops with wisdom and authority.' },
            'wis-end': { 'class': 'worker', 'description': 'A battle-hardened warrior who leads with courage and strength.' },
            'cha-end': { 'class': 'commander', 'description': 'A charismatic and strategic leader, known for their decisive nature and tactical mind.' }
        },
        'fan': {
            'str-int': { 'class': 'battle mage', 'description': 'A mage who combines martial prowess with magical abilities for devastating results.' },
            'str-agi': { 'class': 'monk', 'description': 'A skilled fighter focused on hand-to-hand combat and quick strikes.' },
            'str-wis': { 'class': 'fighter', 'description': 'A strong and resilient warrior, well-versed in a variety of combat styles.' },
            'str-cha': { 'class': 'warlord', 'description': 'A powerful and charismatic guardian who leads their people with might and wisdom.' },
            'str-end': { 'class': 'barbarian', 'description': 'A fierce and untamed warrior who relies on strength and endurance.' },
            'int-agi': { 'class': 'rogue', 'description': 'A stealthy character who specializes in subterfuge, stealth, and surprise attacks.' },
            'int-wis': { 'class': 'shaman', 'description': 'A spiritual and wise nature-based caster who can commune with the elements.' },
            'int-cha': { 'class': 'spy', 'description': 'A covert agent skilled in espionage and gathering vital information.' },
            'int-end': { 'class': 'healer', 'description': 'A dedicated mage focused on healing and supporting allies in battle.' },
            'agi-wis': { 'class': 'thief', 'description': 'A nimble and quick character who specializes in stealth and stealing valuable items.' },
            'agi-cha': { 'class': 'beastmaster', 'description': 'A master of animals, using their bond with creatures to gain an advantage in combat.' },
            'agi-end': { 'class': 'ranger', 'description': 'A guardian skilled in ranged combat and survival in the wild.' },
            'wis-cha': { 'class': 'cleric', 'description': 'A holy mage focused on healing and supporting allies through divine magic.' },
            'wis-end': { 'class': 'druid', 'description': 'A nature-based caster who can shapeshift and command the forces of nature.' },
            'cha-end': { 'class': 'paladin', 'description': 'A noble and righteous warrior who fights for justice and the protection of others.' }
        },
        'pir': {
            'str-int': { 'class': 'corsair', 'description': 'An imperial pirate with a mastery of naval combat and swashbuckling.' },
            'str-agi': { 'class': 'specialist', 'description': 'A versatile pirate skilled in various forms of combat and tactics.' },
            'str-wis': { 'class': 'captain', 'description': 'A seasoned leader who commands a pirate crew with experience and wisdom.' },
            'str-cha': { 'class': 'first-mate', 'description': 'A charismatic and reliable second-in-command aboard a pirate ship.' },
            'str-end': { 'class': 'bouncer', 'description': 'A strong and tough pirate who handles physical confrontations with ease.' },
            'int-agi': { 'class': 'swindler', 'description': 'A cunning and agile pirate who uses deception and trickery to outwit opponents.' },
            'int-wis': { 'class': 'alchemist', 'description': 'A pirate with knowledge of arcane potions and chemicals, useful in combat and healing.' },
            'int-cha': { 'class': 'privateer', 'description': 'A pirate who operates with a sense of honor, often working for the crown.' },
            'int-end': { 'class': 'quartermaster', 'description': 'A pirate in charge of supplies and inventory, ensuring the crew is well-equipped.' },
            'agi-wis': { 'class': 'navigator', 'description': 'A skilled sailor and mapmaker, essential for navigating the high seas.' },
            'agi-cha': { 'class': 'swashbuckler', 'description': 'A daring and charming pirate who excels in close combat with a rapier.' },
            'agi-end': { 'class': 'deckhand', 'description': 'A hardworking pirate who performs essential tasks aboard a ship.' },
            'wis-cha': { 'class': 'witchdoctor', 'description': 'A mystical pirate who uses dark magic and potions to heal and curse others.' },
            'wis-end': { 'class': 'medic', 'description': 'A pirate healer who uses knowledge of anatomy and medicine to tend to injuries.' },
            'cha-end': { 'class': 'pirate lord', 'description': 'A powerful and influential pirate captain, ruling over the high seas.' }
        }
    };

    let combination = `${first_att}-${second_att}`;
    if (class_mapping[set] && class_mapping[set][combination]) {
        console.log("Combination: ", combination)
        return class_mapping[set][combination];
    }

    combination = `${second_att}-${first_att}`;
    if (class_mapping[set] && class_mapping[set][combination]) {
        console.log("Combination: ", combination)
        return class_mapping[set][combination];
    }

    return "Class not found for the given attributes and theme.";
}
function get_personality_name(MBTI) {
    console.log('Personality_Name MBTI: ', MBTI);
    var personalities = {
        'INTJ': ['The Architect', 'Approach: Logical, strategic, prefers long-term solutions.\nGameplay Impact: Might approach negotiations with a meticulous, calculated strategy, opting for planned, methodical discussions.\nThese players would excel in situations requiring a clear, logical argument but might struggle in emotionally charged situations.\nPossible Scenarios: "Negotiate the terms using hard data," "Create a strategic alliance for future gain," "Advocate for a systemized solution."'],
        
        'INTP': ['The Thinker', 'Approach: Inventive, curious, loves abstract ideas and theories.\nGameplay Impact: Likely to take a more unconventional approach in dialogue, proposing creative but perhaps impractical solutions. They may question authority and challenge the status quo, which could result in conflict or new opportunities.\nPossible Choices: "Explore a theoretical solution to the issue," "Challenge assumptions and propose something radical," "Consider an alternative perspective."'],
        
        'ENTJ': ['The Commander', 'Approach: Assertive, determined, focused on results.\nGameplay Impact: Characters with this personality would have strong, forceful dialogue options, demanding respect and pushing for quick, decisive action. They may try to impose their will on situations and could face resistance or admiration depending on the outcome.\nPossible Choices: "Take charge of the situation and dictate terms," "Leverage authority to bend the rules," "Take immediate action to secure a victory."'],
        
        'ENTP': ['The Debater', 'Approach: Outspoken, enjoys arguing and testing ideas.\nGameplay Impact: Known for being persuasive, they might engage in witty or sarcastic repartee during diplomatic situations. The Debater could turn confrontations into debates, potentially winning allies through charm or sharp arguments.\nPossible Choices: "Debate the other party into submission," "Challenge the opposing argument with logic," "Play devil\'s advocate to get more information."'],
        
        'INFJ': ['The Advocate', 'Approach: Insightful, empathetic, values deep connections.\nGameplay Impact: Empathetic dialogue options, often trying to mediate between conflicting sides. Advocates will be drawn to moral causes and seeking pragmatic, cooperative solutions that benefit everyone. However, they may avoid direct confrontation, opting for indirect solutions.\nPossible Choices: "Appeal to the other party\'s sense of morality," "Find common ground through shared values," "Create a peaceful compromise."'],
        
        'INFP': ['The Mediator', 'Approach: Idealistic, values harmony and understanding.\nGameplay Impact: Soft-spoken and diplomatic, likely to offer creative, peaceful solutions. INFPs might avoid conflict or work towards emotional resolution rather than practical outcomes. This could be both an advantage and a disadvantage, depending on the scenario.\nPossible Choices: "Find a win-win scenario for both sides," "Encourage mutual understanding through storytelling," "Diffuse tension with compassion."'],
        
        'ENFJ': ['The Protagonist', 'Approach: Charismatic, socially aware, strong leadership skills.\nGameplay Impact: Protagonists will naturally engage in people-focused diplomacy, working to rally support for their cause and using their charisma to bring others into their vision. They would excel in motivating others but could be too idealistic at times.\nPossible Choices: "Inspire the group to take action together," "Lead with compassion and warmth," "Offer solutions that cater to everyone\'s needs."'],
        
        'ENFP': ['The Campaigner', 'Approach: Campaigners are creative, spontaneous, and value freedom.\nGameplay Impact: Known for their enthusiastic, optimistic approach to challenges. They might try to find a fun, unconventional solution to a diplomatic issue, preferring creative, flexible thinking over rigid rules.\nPossible Choices: "Use charm and enthusiasm to sway opinions," "Think outside the box to win over the crowd," "Offer a lighthearted, flexible solution."'],
        
        'ISTJ': ['The Logistician', 'Approach: Practical, dependable, values tradition.\nGameplay Impact: Logisticians will likely approach diplomatic situations with a strong sense of duty and an adherence to rules. They prefer clear, organized solutions and will avoid ambiguity.\nPossible Choices: "Propose a tried-and-true solution," "Stick to tradition and established norms," "Offer a detailed, step-by-step plan."'],
        
        'ISFJ': ['The Defender', 'Approach: Loyal, supportive, focuses on security.\nGameplay Impact: Defenders are service-oriented, often putting others\' needs first. In a diplomatic context, they will likely mediate and support the needs of others rather than assert their own will.\nPossible Choices: "Advocate for the protection of those who need help," "Ensure everyone\'s safety before proceeding," "Create a solution that preserves stability and order."'],
        
        'ESTJ': ['The Executive', 'Approach: Efficient, organized, prefers structure and authority.\nGameplay Impact: Executives are likely to be straightforward and practical, preferring decisive actions that are well-planned. They would excel in roles where they can take charge and lead with authority.\nPossible Choices: "Make a decision and implement it immediately," "Organize the team to complete the task effectively," "Stick to a well-structured plan."'],
        
        'ESFJ': ['The Consul', 'Approach: Social, caring, values cooperation.\nGameplay Impact: Consuls are likely to seek cooperative, peaceful solutions, relying on their strong interpersonal skills. They may work to ensure everyone is happy and included, sometimes at the cost of more practical or idealistic goals.\nPossible Choices: "Appeal to the group\'s sense of community," "Find a consensus that everyone can agree on," "Ensure that no one is left behind in the discussion."'],
        
        'ISTP': ['The Virtuoso', 'Approach: Analytical, flexible, enjoys hands-on problem solving.\nGameplay Impact: Virtuosos are likely to approach diplomatic situations with pragmatism and flexibility, often looking for solutions based on action rather than words. They might favor direct solutions that require little negotiation.\nPossible Choices: "Find a practical solution that requires action," "Use logic to simplify the situation," "Make quick decisions and adapt as things change."'],
        
        'ISFP': ['The Adventurer', 'Approach: Artistic, gentle, values personal freedom.\nGameplay Impact: Adventurers would focus on harmonious, creative solutions to diplomacy, offering peaceful ways to resolve conflict. They may have a more emotional, heartfelt approach to negotiations.\nPossible Choices: "Appeal to the emotions of others," "Use creativity to inspire a peaceful resolution," "Suggest a flexible, open-ended compromise."'],
        
        'ESTP': ['The Entrepreneur', 'Approach: Energetic, bold, enjoys excitement.\nGameplay Impact: Entrepreneurs are likely to engage with a bold, spontaneous approach. They thrive in action-oriented environments and may push for immediate solutions, sometimes foregoing diplomacy in favor of action.\nPossible Choices: "Take action without waiting for consensus," "Challenge others to make a quick decision," "Push forward with a bold plan."'],
        
        'ESFP': ['The Entertainer', 'Approach: Fun-loving, spontaneous, enjoys the moment.\nGameplay Impact: Entertainers would likely use charismatic charm to win over others and create a fun, easygoing atmosphere. They may use humor and lightheartedness to diffuse tension, although they can command more serious confrontations.\nPossible Choices: "Lighten the mood with humor," "Charm the group into agreeing with your idea," "Suggest a spontaneous, fun solution to the problem."']
    };
    if (!personalities[MBTI]) {
        console.error("No personality found for MBTI:", MBTI);  
        return ['Unknown', 'Description not found'];
    }

    console.log('What should return: ', personalities[MBTI]);
    return personalities[MBTI];
}

function discover(desc, att) {
    var person_scores = Object.entries(character_data.att).slice(6, 14)
    var desc_weight = 0.7 
    var att_weight = 0.3 

    var att_modifiers = {
        'intelligence': [-2, -2, -3, 1],  
        'strength': [1, -2, -1, -1],       
        'endurance': [-1, -3, -2, 1],      
        'charisma': [3, 2, 3, 1],         
        'wisdom': [1, 2, 2, -1],           
        'agility': [-1, 2, 2, -1]            
    };

    var clean_desc = desc.trim() === "" ? "bold energetic free reflective risktaking decisive independent character" : desc.replace(/[^\w\s]/g, '');

    var E = ['outgoing','charismatic','bold','social','adventurous','energetic','talkative','expressive','leader','optimistic','enthusiastic','engaging','funloving','gregarious','assertive'];
    var I = ['quiet','reflective','thoughtful','reserved','independent','observant','contemplative','private','mysterious','shy','introspective','calm','focused','selfsufficient','self','serene'];

    var N = ['imaginative','visionary','creative','abstract','theoretical','insightful','curious','innovative','future','idealistic','conceptual','dreamer','pattern','reflective', 'imagination', 'vision']; 
    var S = ['practical','realistic','detail','observant','grounded','logical','concrete','present','action','reliable','precise','sensible','cautious','hands','focused', 'dirty', 'mess', 'clean', 'touch']; 

    var F = ['compassionate','empathetic','caring','sensitive','altruistic','harmonious','supportive','kind','heart','idealistic','genuine','considerate','patient','warm','understanding','cooperative'];
    var T = ['Analytical','logical','objective','strategic','decisive','detached','independent','rational','problemsolver','solver','skeptical','critical','realistic','efficient','pragmatic','direct', 'smart'];

    var P = ['spontaneous','flexible','openminded','open','adaptable','curious','freespirited','free','playful','resourceful','creative','unconventional','disorganized','exploratory','risktaking','risk','innovative','carefree','careless']; 
    var J = ['organized','structured','responsible','decisive','planner','disciplined','systematic','goaloriented','goal','reliable','focused','efficient','methodical','conscientious','punctual','predictable'];

    Object.keys(att).forEach(function(attribute) {
        if (att_modifiers[attribute]) {
            var modifiers = att_modifiers[attribute];

            person_scores[0] += modifiers[0] * att_weight
            person_scores[1] -= modifiers[0] * att_weight
            
            person_scores[2] += modifiers[1] * att_weight
            person_scores[3] -= modifiers[1] * att_weight
            
            person_scores[4] += modifiers[2] * att_weight
            person_scores[5] -= modifiers[2] * att_weight

            person_scores[6] += modifiers[3] * att_weight
            person_scores[7] -= modifiers[3] * att_weight
        }  
    })
    var clean_desc = desc.replace(/[^\w\s]/g, '');
    var desc_words = clean_desc.split(' ') 

    desc_words.forEach(function(word) {
        if (E.includes(word)) person_scores[0] += desc_weight;
        if (I.includes(word)) person_scores[1] += desc_weight;
        if (N.includes(word)) person_scores[2] += desc_weight;
        if (S.includes(word)) person_scores[3] += desc_weight;
        if (F.includes(word)) person_scores[4] += desc_weight;
        if (T.includes(word)) person_scores[5] += desc_weight;
        if (P.includes(word)) person_scores[6] += desc_weight;
        if (J.includes(word)) person_scores[7] += desc_weight;
    });

    for (var i = 0; i < 8; i++) {
        person_scores[i] = person_scores[i] * desc_weight + person_scores[i] * att_weight;
    }

    var e_i = person_scores[0] > person_scores[1] ? "E" : "I"
    var n_s = person_scores[3] > person_scores[2] ? "S" : "N"
    var f_t = person_scores[4] > person_scores[5] ? "F" : "T"
    var p_j = person_scores[7] > person_scores[6] ? "J" : "P"

    var MBTI = (e_i+n_s+f_t+p_j);
    console.log('MBTI: ', MBTI)
    var type = get_personality_name(MBTI);

    return [type[0], type[1], MBTI];
}
function updateQuestion() {
    let questionContainer = document.getElementById("question-title");
    let optionsContainer = document.getElementById("options-container");
    let nextButton = document.getElementById("quiz-button");

    // Clear previous options
    optionsContainer.innerHTML = "";

    // Show the current question
    questionContainer.innerHTML = app_questions[curr_question].question;

    // Create radio buttons for each option
    app_questions[curr_question].options.forEach((option, index) => {
        let optionLabel = document.createElement("label");
        let optionInput = document.createElement("input");
        optionInput.type = "radio";
        optionInput.name = "question" + curr_question; // Ensure only one selection per question
        optionInput.value = option.attributes; // Value contains attribute updates
        optionLabel.appendChild(optionInput);
        optionLabel.appendChild(document.createTextNode(option.text));
        optionsContainer.appendChild(optionLabel);
        optionsContainer.appendChild(document.createElement("br"));
    });

    // Next button event handler
    nextButton.onclick = function() {
        // Get selected radio button
        let selectedOption = document.querySelector('input[name="question' + curr_question + '"]:checked');

        if (!selectedOption) {
            alert("Please select an option!");
            return;
        }

        // Update the attributes based on the selected option
        let attributes = selectedOption.value.split(",");
        for (let i = 0; i < attributes.length; i += 2) {
            let attribute = attributes[i];
            let value = parseInt(attributes[i + 1]);
            if (!character_data.att[attribute]) {
                character_data.att[attribute] = 0;
            }
            character_data.att[attribute] += value;
        }

        // Move to the next question or calculate the class if it's the last question
        curr_question++;
        if (curr_question < app_questions.length) {
            updateQuestion(); // Update the UI with the next question
        } else if (curr_question === app_questions,length) {
            document.getElementById('quiz-button').innerHTML = "Submit";
            updateQuestion();
        } else {
            // All questions have been answered, calculate the class
            calculateClass();
        }
    };
}
function sort(dict) {
    console.log("Sorting Entries: ", dict)
    entries = dict.sort((a, b) => b[1] - a[1]);

    return entries.map(entry => entry.slice(0, 3)); 
}
function calculateClass() {
    const quiz_button = document.getElementById("quiz-button");
    let character_att = Object.entries(character_data.att).slice(0, 6);
    console.log("Attribute Entries: ", character_att);
    sortedAttributes = sort(character_att, true);
    console.log("Sorted Attributes: ", sortedAttributes);
    let topEntries = sortedAttributes.slice(0, 2);
    console.log("Top Entries: ", topEntries);
    let topAttributesLong = topEntries.map(entry => entry[0]);
    console.log("Top Attributes: ", topAttributesLong);
    let topAttributes = topAttributesLong.map(attr => attr.slice(0, 3));
    console.log("Shortened Top Attributes: ", topAttributes)

    // Use class_check function to determine the class based on attributes and theme
    let character_class = class_check(topAttributes, selectedSet);
    console.log("Character Class: ", character_class)

    // Update character class and description
    character_data.class = character_class.class;
    character_data.description = character_class.description;

    console.log("Top Attributes: ", topAttributes)

    // Display the result
    if (!character_data.att || Object.keys(character_data.att).length === 0) {
        document.getElementById("question-title").innerHTML = "Attributes are empty.";
    } else {
        let attributesContainer = document.getElementById("attributes-container");
        attributesContainer.style.display= "block";
    
        for (let attr in character_data.att) {
            if (character_data.att.hasOwnProperty(attr)) {
                let valueLabel = document.createElement("label");
                valueLabel.textContent = `${attr}: ${character_data.att[attr]}`;
                attributesContainer.appendChild(valueLabel);
            }
        }
    }

    document.getElementById("question-title").innerHTML = `Your character's class is: ${character_class.class}`;
    document.getElementById("options-container").innerHTML = `Description: ${character_class.description}`;
    quiz_button.innerHTML = "Submit";
    quiz_button.onclick = showDescription;
}

// Initialize the questionnaire (to be called after the initial selection)
function startQuestionnaire() {
    curr_question = 0;
    document.getElementById('quiz-ask').style.display = 'none';
    document.getElementById('question-title').style.display = 'flex';
    document.getElementById('options-container').style.display = 'grid';
    document.getElementById('quiz-button').style.display = 'block';
    updateQuestion(); // Show the first question
}
function showDescription() {
    document.getElementById("quiz-box").style.display = 'none';
    document.getElementById("desc-box").style.display = "grid";
}
function nextStep(currStep) {
    if (currStep === 3) {
        if (selectedAttributes.length > 2) {
            alert('Only two attributes can be selected');
            return;
        }
        else if (selectedAttributes.length < 2) {
            alert('You must select Two(2) Attributes.');
            return;
        }
        for (let i; i < selectedAttributes.length; i++) {
            character_data[att, selectedAttributes[i]] + 1;
        }
    }
    if (currStep === 4) {
        var person_name;
        var person_desc;
        var person_type;
        var name_plate = document.getElementById('character_name');
        var personality_label = document.getElementById('personality_name');
        var person_desc_label = document.getElementById('personality_description');
        var class_label = document.getElementById('class_name');
        var class_desc_label = document.getElementById('class_description');
        const charDesc = document.getElementById('character_desc').value;

        var personality = discover(charDesc, sortedAttributes);
        person_name = personality[0];
        person_desc = personality[1];
        person_type = personality[2];
        console.log('Returned Discover Variable: ', personality)
        console.log("Personality Name: ", person_name)

        name_plate.innerHTML = character_data.name;
        personality_label.innerHTML = title(person_name);
        person_desc_label.innerHTML = person_desc;
        class_label.innerHTML = character_data.class;
        class_desc_label.innerHTML = character_data.description;
    }

    document.getElementById(`step${currStep}`).style.display = 'none';
    currStep += 1;
    document.getElementById(`step${currStep}`).style.display = 'block'; 
}
function checkName() {
    var nameValue = document.getElementById('name').value.trim();
    
    var names = nameValue.split(' ');

    if (nameValue === "") {
        alert("Please enter a Character Name");
        return;
    }

    if (names.length > 3) {
        alert("Too Many Names : Only First, Middle, and Last Names seperated by spaces are allowed, please follow that format");
        return;
    }

    if (names.length === 1) {
        character_data.first_name = title(names[0]);
    } else if (names.length === 2) {
        character_data.first_name = title(names[0]);
        character_data.last_name = title(names[1]);
        character_data.name = [character_data.first_name, character_data.last_name].join(' ');
    } else if (names.length === 3) {
        character_data.first_name = title(names[0]);
        character_data.middle_name = title(names[1]);
        character_data.last_name = title(names[2]);
        character_data.name = [character_data.first_name, character_data.middle_name, character_data.last_name].join(' ');
    }

    document.getElementById('step1').style.display = 'none';
    document.getElementById('step2').style.display = 'block';
}
function updateAttributes() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    selectedAttributes = [];
    selectedSet = document.getElementById('theme').value;
    
    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            selectedAttributes.push(checkbox.value);
        }
    });

    if (selectedAttributes.length === 1) {
        return;
    }

    var character_class = class_check(selectedAttributes, selectedSet);
    
    if (typeof character_class === 'object' && character_class !== null) {
        character_data.class = character_class.class;
        character_data.description = character_class.description;

        document.getElementById('class-title').innerHTML = title(character_class.class);
    } else {
        console.error("Class not found for the given attributes and theme.");
        document.getElementById('class-title').innerHTML = "Class not found";
    }
}
// Additional text to recommit