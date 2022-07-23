init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_hangout",
            prompt="I'm going to hangout with friends.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_hangout:
    m "Oh, you are?"
    m "How I wish I could go with you..."
    m "I would love to meet your friends! After all, they make my [player] very happy, don't they?"
    m "Have fun [mas_get_player_nickname()]!"
    
return "quit"
