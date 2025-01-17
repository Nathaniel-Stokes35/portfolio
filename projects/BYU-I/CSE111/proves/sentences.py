import random
def main():
    make_sentence(tense='past')
    make_sentence()
    make_sentence(tense='future')
    make_sentence(True, 'past')
    make_sentence(True)
    make_sentence(True, 'future')

def make_sentence(plural=False, tense='present'):
    det = get_determiner(plural)
    noun = get_noun(plural)
    adj = get_adjective()
    verb = get_verb(plural, tense)
    adv = get_adverb()
    phrase = get_prepositional_phrase(plural)
    phrase2 = get_prepositional_phrase(plural)
    print(f'{det} {adj} {noun}{phrase2}, {adv} {verb}{phrase}.'.capitalize())

def get_determiner(plural=False):
    if plural:
        options = ['Some', 'Many', 'The', 'All', 'A few', 'Most']
    else:
        options = ['The', 'My', 'Your', 'His', 'Her', 'It\'s', 'Our']
    return (random.choice(options))

def get_noun(plural=False):
    if plural:
        options = ['cats', 'children', 'creatives', 'parents', 'singers', '"exotic people"', 'dogs']
    else:
        options = ['choosen one', 'cat', 'neighbor', 'child', 'eternal companion', 'favorite bird', 'noun']
    return (random.choice(options))

def get_adjective():
    options = ["quick", "tall", "smart", "greedy", "belligerent",
                "stoic", "grounded", "witty", "quick-tempered", "condescending",
                "mighty", "mystical", "happy", "extroverted", "introverted",
                "weary", "ominous", "interesting", "misinformed", "unadjusted",
                "odd", "creative", "helpful", "official", "musical",
                "forgotten", "disingenuous", "misplaced", "hypocritical", "loving"]
    return(random.choice(options))

def get_adverb():
    options = ["quickly", "effectively", "intelligently", "greedily", "belligerently",
                "stoically", "firmly", "cleverly", "timidly", "condescendingly",
                "mightily", "mystically", "happily", "socially", "abrasively",
                "wearily", "ominously", "interestingly", "unabashedly", "caringly",
                "oddly", "creatively", "helpfully", "officially", "musically",
                "comfortably", "disingenuously", "excitedly", "hypocritically", "lovingly"]
    return(random.choice(options))

def get_verb(plural=False, tense='present'):
    if plural:
        if tense == 'past':
            options = ['loved', 'lost', 'cried', 'smiled', 'laughed', 'have corrupted bueracrats across the country', 'have left']
        elif tense == 'present':
            options = ['swim', 'smile', 'leave', 'hit', 'bite', 'think quickly', 'plagerize']
        else:
            options = ['will establish a strong bourgeoisie', 'will laugh menicingly at small childen', 'will cry at the second coming', 'will have a car', 'will have been traveling', 'will be working', 'will be staying the night']
    else:
        if tense == 'past':
            options = ['worked', 'ran', 'played', 'wept at the state of the country', 'bagan to code', 'solved the puzzle', 'ran into a wall']
        elif tense == 'present':
            options = ['cleans', 'plays', 'studies', 'writes', 'runs', 'works', 'grades']
        else:
            options = ['will walk', 'will learn', 'will study', 'will grade', 'will program an AI model', 'will follow-up', 'will help']
    return (random.choice(options))

def get_preposition():
    options = ["about", "above", "across", "after", "along",
                "around", "at", "before", "behind", "below",
                "beyond", "by", "despite", "except", "for",
                "from", "in", "into", "near", "of",
                "off", "on", "onto", "out", "over",
                "past", "to", "under", "with", "without"]
    return (random.choice(options))

def get_prepositional_phrase(plural=False):
    prep = get_preposition() 
    det = get_determiner(plural)
    adj = get_adjective() 
    noun = get_noun(plural)
    return (f', {prep} {det} {adj} {noun}')

main()