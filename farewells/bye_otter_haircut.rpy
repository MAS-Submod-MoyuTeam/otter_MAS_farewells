init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_haircut",
            prompt="I'm going to have a haircut.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_haircut:
    m 2wuo "Oh!"
    m 2rksdra "How I wish I could see it..."
    m 2hubla "Though I'm sure it will look amazing, [player]."
    m 2hublb "See you later!"
    
return "quit"
