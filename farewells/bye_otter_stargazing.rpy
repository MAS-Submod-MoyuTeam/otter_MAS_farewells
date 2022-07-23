init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_stargazing",
            prompt="I'm going stargazing.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_stargazing:
    m 1wuo "Oh, you are?"
    m 2rksdra "How I wish I could go with you... It's one of my dreams, after all..."
    m 7hub "I would love to lay on your chest and look into the stars together! One day, [player], one day..."
    m 2hub "Have fun [mas_get_player_nickname()]!"
    
return "quit"
