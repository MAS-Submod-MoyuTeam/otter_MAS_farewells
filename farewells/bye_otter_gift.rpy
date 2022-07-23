init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_otter_gift",
            prompt="I'm going to prepare you some gifts.",
            unlocked=True,
        ),
        code="BYE"
    )

label bye_otter_gift:
    m 1sublo "You are?"
    m 1hublb "You're too kind, [player]."
    m 7hublb "You know I love when you take your time to gift me things."
    m 2sublb "I'm excited to see what you're gonna give me this time!"
    m 2hubla "See you soon!"

return "quit"
