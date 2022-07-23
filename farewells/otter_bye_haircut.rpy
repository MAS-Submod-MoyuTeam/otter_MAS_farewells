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
    m "Oh!"
    m "How I wish I could see it..."
    m "Though I'm sure it will look amazing, [player]."
    m "See you later!"
    
return "quit"
