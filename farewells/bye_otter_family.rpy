init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_family",
            prompt="I'm going to spend time with family.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_family:
    m 1eub "Aww, that's great, [player]!"
    m 7hua "Family is very important, after all."
    m "I hope you have a great time with them!"
    m 1eub "See you later!"
    
return "quit"
