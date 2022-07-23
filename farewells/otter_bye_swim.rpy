init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_swim",
            prompt="I'm going for a swim.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_swim:
    m "Ooh, how refreshing!"
    m "Have fun, [player]!"
    m "I'll see you later."
    
return "quit"
