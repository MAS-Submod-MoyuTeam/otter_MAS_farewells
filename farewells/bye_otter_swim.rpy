init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_swim",
            prompt="I'm going for a swim.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_swim:
    m 1wuo "Ooh, how refreshing!"
    m 2hub "Have fun, [player]!"
    m 2eua "I'll see you later."
    
return "quit"
