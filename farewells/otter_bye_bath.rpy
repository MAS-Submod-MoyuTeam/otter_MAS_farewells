init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_bath",
            prompt="I'm going to take a bath.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_bath:
    m "Ooh, how relaxing!"
    m "Have a great one, [player]!"
    m "Make sure to take this time to relax."
    m "See you later!"
    
return "quit"
