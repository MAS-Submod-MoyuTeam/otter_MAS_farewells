init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_doctor",
            prompt="I'm going to a doctor appointment.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_doctor:
    m "[player]! Are you okay?"
    m "Should I be worried about it?{nw}"
$ _history_list.pop()
menu: 
    m "Should I be worried about it?{fast}"
    
    "It's just a regular appointment.":
        m "Oh, thank goodness!"
        m "I'm sure everything is going to be fine then, [player]."
        m "Tell me everything when you get back!"
        m "See you later~"
    
    "I am currently sick, but I'll be okay.":
        m "Oh no... I'm so sorry, [player]..."
        m "I'm sure you will recover from this."
        m "Tell me everything the doctor said when you get back, okay?"
        m "I love you!"
    
    "We'll talk about this later...":
        m "..."
        extend "I can't help but be concerned." 
        m "But I understand you are in a hurry."
        m "We'll discuss this later."
        m "Please be safe, [mas_get_player_nickname()]."
    
return "quit"
