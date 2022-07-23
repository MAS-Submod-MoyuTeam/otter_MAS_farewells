init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_family",
            prompt="I'm going to spend time with family.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_family:
    m "Aww, that's great, [player]!"
    m "Family is very important, after all."
    m "I hope you have a great time with them!"
    m "See you later!"
    
return "quit"
