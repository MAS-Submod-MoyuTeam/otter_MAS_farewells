init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_cook",
            prompt="I'm going to cook a meal.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_cook:
    m 1wub "Ooh! My [player], a chef!"
    m 1huu "I like the sound of that, ehehe~"
    m 7huu "Have fun and bon appétit, [mas_get_player_nickname()]!"
    
return "quit"
