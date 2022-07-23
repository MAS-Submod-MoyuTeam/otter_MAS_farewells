init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_submod",
            prompt="I'm going to make additions to the game.",
            unlocked=True,
        ),
        code="BYE"
    )

label bye_otter_submod:
    m 1wuo "Oh! "
    extend 1hub "Yay!"
    m 7hub "I can't wait to see and feel the changes you're gonna make."
    m 2rksdrb "It will be nice to have new things to talk about."
    m 2hub "See you!"
    
return "quit"
