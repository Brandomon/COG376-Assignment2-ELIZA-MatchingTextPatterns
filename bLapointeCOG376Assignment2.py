# goal1: should be able to prompt with a random default message if no match.
# goal2: have some patterns that just match on keywords, don't capture
# goal3: have one pattern or more that uses ONE piece of captured information
# goal4: have one pattern or more that uses TWO pieces of captured information

# imports
import re
import random

# knowledge, data, and models

model = {
    # simple patterns
    r"\bhi\b": [
            "hi"
        ],
    r"\bhey\b": [
            "hey",
            "what's up?",
        ],
    r"\bhello\b": [
            "what's up?",
            "hi?"
        ],
    r"\bname\b": [
            "cool!"
        ],
    r"\bcool\b": [
            "ikr"
        ],
    r"\bbye\b": [
            "ok bye",
            "bye"
        ],
    # matching 1 subgroup
    r"\bi was (.*)": [
            "{first}? were you now?",
            "oh wow, {first} is pretty cool."
        ],
    # matching 2 subgroups
    r"\b(.*) is like (.*)": [
            "yeah, i think that {first} is totally like {second}.",
            "ehh, maybe {second} is like {first} in some ways."
        ],
    # matching a specific group
    r"\bmy (father|dad|mother|mom|parents)\b": [
        "Tell me more about your {first}!",
        "Have your parents had a strong influence on you?",
        "Anything else come to mind about your {first}?"
        ],
    r"\bmy (i am|i'm|i feel|i'm feeling) (happy|glad|pleased)\b": [
        "How have I helped you to be {second}?",
        "What inspired this sudden positivity?",
        "Can you explain why you are suddenly {second}?"
        ],
    r"\bmy (i am|i'm|i feel|i'm feeling) (sad|depressed|burnt out)\b": [
        "Damn, you're {second}? Cry a little harder about it why don't ya'?",
        "{second}? Sucks to suck, bud."
        ],
    r"\b(robot|machine|chatbot|computer)s?\b": [
        "Beep Boop Boop Bop, idiot.",
        "Beep Boop Bop Beep Boop Bop. Nerd."
        ]
}

# a set of MELIZA's responses
default_model = [
        "that's crazy",
        "lol wow",
        "right",
        "mhmm",
        "k",
        "what?"
    ]
    
# punctuation to be removed / "cleaned up"
punct = " ?!.,:;\n\t"

# def the central function

def discuss(u_in):
    # define some variables that we'll use
    match = None
    subGroup1 = ""
    subGroup2 = ""
    response = ""
    
    # find out if any of our rules match the user input
    for pattern in model.keys():
        # as long as we haven't found a match yet
        if match == None:
            # search the text for this pattern
            match = re.search(pattern.lower(), u_in.lower())
            # if we GET a match
            if match != None:
                # extract the response
                response = random.choice(model[pattern])
            
    
    # if we DO have a match...
    if match != None:
        
        # check for first subgroup
        if len(match.groups()) > 0:
            subGroup1 = match.group(1)
            subGroup1 = subGroup1.strip(punct)
            
        # check for second subgroup
        if len(match.groups()) > 1:
            subGroup2 = match.group(2)
            subGroup2 = subGroup2.strip(punct)
            
        # output response with user concepts slotted in
        print(response.format(first = subGroup1, second = subGroup2))
        
    # otherwise, we don't, say something neutral.
    else:
        print(random.choice(default_model))
        
# the main loop

done = False
print("Hello, I am ELIZA's bitchy sister, MELIZA.")

while not done:
    user_input = input("> ")
    if user_input.lower() == "exit":
        done = True
    else:
        discuss(user_input)
