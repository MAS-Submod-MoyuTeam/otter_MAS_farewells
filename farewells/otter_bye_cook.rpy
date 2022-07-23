init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_cook",
            prompt="I'm going to cook a meal.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_cook:
    m "Ooh! My [player], a chef!"
    m "I like the sound of that, ehehe~"
    m "Have fun and bon appétit, [mas_get_player_nickname()]!"
    
return "quit"
