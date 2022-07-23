init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_doctor",
            prompt="I'm going to a doctor appointment.",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_otter_doctor:
    m 1wud "[player]! Are you okay?"
    m 1wusdrc "Should I be worried about it?{nw}"
$ _history_list.pop()
menu: 
    m "Should I be worried about it?{fast}"
    
    "It's just a regular appointment.":
        m 1hub "Oh, thank goodness!"
        m 1eub "I'm sure everything is going to be fine then, [player]."
        m 7hub "Tell me everything when you get back!"
        m 7hua "See you later~"
    
    "I am currently sick, but I'll be okay.":
        m 1eksdrd "Oh no... I'm so sorry, [player]..."
        m 7eksdra "I'm sure you will soon recover from this."
        m 7hka "Tell me everything the doctor said when you get back, okay?"
        m 1hub "I love you!"
    
    "We'll talk about this later...":
        m 1dksdrc "..."
        extend 1dksdrd "I can't help but be concerned." 
        m 1rksdrd "But I understand you are in a hurry."
        m 1eksdrd "We'll discuss this later."
        m "Please be safe, [mas_get_player_nickname()]."
    
return "quit"
