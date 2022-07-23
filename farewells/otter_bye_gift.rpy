init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="otter_bye_gift",
            prompt="I'm going to prepare you some gifts.",
            unlocked=True,
        ),
        code="BYE"
    )

label otter_bye_gift:
    m "You are?"
    m "You're too kind, [player]."
    m "You know I love when you take your time to gift me things."
    m "I'm excited to see what you're gonna give me this time!"
    m "See you soon!"

return "quit"
