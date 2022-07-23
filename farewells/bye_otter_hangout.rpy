init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_hangout",
            prompt="I'm going to hangout with friends.",
            unlocked=True,
        ),
        code="BYE"
    )

label bye_otter_hangout:
    m 1wuo "Oh, you are?"
    m 2rksdra "How I wish I could go with you..."
    m 7hub "I would love to meet your friends! After all, they make my [player] very happy, don't they?"
    m 2hub "Have fun [mas_get_player_nickname()]!"
    
return "quit"
