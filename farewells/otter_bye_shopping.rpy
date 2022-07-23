init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_shopping",
            prompt="I'm going to prepare you some gifts.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_shopping:
    m "How fun, [player]!"
    m "Make sure to buy lots of great stuff."
    m "And to have fun, too!"
    m "See you later!"
    
return "quit"
