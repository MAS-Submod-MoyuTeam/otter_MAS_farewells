init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_haircut",
            prompt="I'm going to have a haircut.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_haircut:
    m 2wuo "Oh!"
    m 2rksdra "How I wish I could see it..."
    m 2hubla "Though I'm sure it will look amazing, [player]."
    m 2hublb "See you later!"
    
return "quit"
