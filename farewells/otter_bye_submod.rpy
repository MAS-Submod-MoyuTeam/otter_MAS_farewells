init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_submod",
            prompt="I'm going to make additions to the game.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_submod:
    m "Oh! "
    extend "Yay!"
    m "I can't wait to see and feel the changes you're gonna make."
    m "It will be nice to have new things to talk about."
    m "See you!"
    
return "quit"
