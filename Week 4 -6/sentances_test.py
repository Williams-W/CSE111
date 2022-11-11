from sentances import get_determiner , get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import pytest

def test_get_determiner():
    
    single_determiners = ["a", "one", "the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    plural_determiners = ["some", "many", "the"]

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():
    verb_past = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1, "past")
        assert verb in verb_past

    single_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")
        assert verb in single_present

    plural_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(3, "present")
        assert verb in plural_present

    verb_future = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, "future")
        assert verb in verb_future

def test_get_preposition():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in preposition

def test_prepositional_phrase():
    preposition = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    determiner = ["a", "one", "the","some", "many", "the"]
    

    for _ in range(4):
        single_prepositional_phrase = get_prepositional_phrase(1)
        parts = str.split(single_prepositional_phrase)
        parts_len = len(str.split(single_prepositional_phrase))
        assert parts[0] in preposition
        assert parts[1] in determiner
        assert parts[2] in noun
        assert parts_len == 3

    for _ in range(4):
        plural_prepositional_phrase = get_prepositional_phrase(2)
        parts = str.split(single_prepositional_phrase)
        parts_len = len(str.split(plural_prepositional_phrase))
        assert parts[0] in preposition
        assert parts[1] in determiner
        assert parts[2] in noun
        assert parts_len == 3

def test_get_adjective():
    adjectives = ["blue", "green", "large", "small", "scary", "beautiful", "red", "shiny", "dead",
    "dull", "evil", "fancy", "filthy", "homeless", "plain" ]
    for _ in range(4):
        word = get_adjective()
        assert word in adjectives
pytest.main(["-v", "--tb=line", "-rN", __file__])

