init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_shopping",
            prompt="I'm going to prepare you some gifts.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_shopping:
    m 7wua "How fun, [player]!"
    m 7hua "Make sure to buy lots of great stuff."
    m 2hub "And to have fun, too!"
    m 2eub "See you later!"
    
return "quit"
