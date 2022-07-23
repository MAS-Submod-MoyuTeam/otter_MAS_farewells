init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_walk",
            prompt="I'm going for a walk.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_walk:
    m 7wua "How fun, [player]!"
    m 7hua "Make sure to take a bottle of water with you."
    m 2hub "And be safe, okay?"
    m 2eub "See you later!"
    
return "quit"
