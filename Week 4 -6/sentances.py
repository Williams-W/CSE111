import random

def main():
    tense = ["past", "present", "future"]

    for x in tense:
            quantity = 1
            tense_for = x
            d = get_determiner(quantity)
            a = get_adjective()
            n = get_noun(quantity)
            v = get_verb(quantity, tense_for)
            p_p = get_prepositional_phrase(quantity)
            print(d, a, n, v, p_p)

    for x in tense:
            quantity = 2
            tense_for = x
            d = get_determiner(quantity)
            a = get_adjective()
            n = get_noun(quantity)
            v = get_verb(quantity, tense_for)
            p_p = get_prepositional_phrase(quantity)
            print(d, a, n, v, p_p)

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    noun = random.choice(noun)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
        
    elif tense == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        
    elif tense == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    
    elif tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verb)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition = get_preposition()

    prepositional_phrase = preposition + " " + determiner  +" "+ noun
    return prepositional_phrase

def get_adjective():
    adjectives = ["blue", "green", "large", "small", "scary", "beautiful", "red", "shiny", "dead",
    "dull", "evil", "fancy", "filthy", "homeless", "plain" ]
    adjective = random.choice(adjectives)
    return adjective

if __name__ == "__main__":
    main()
