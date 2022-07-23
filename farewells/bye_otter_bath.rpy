init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_bath",
            prompt="I'm going to take a bath.",
            unlocked=True,
        ),
        code="BYE"
    )

label bye_otter_bath:
    m 1wub "Ooh, how relaxing!"
    m 1wub "Have a great one, [player]!"
    m "Make sure to take this time to relax."
    m 6fua "See you later!"
    
return "quit"
