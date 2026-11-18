#!/usr/bin/env python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not isinstance(attendees, list):
        print("invalid input: attendees must be a list")
        return
    if not all(isinstance(item, dict) for item in attendees):
        print("Invalid input: attendees must be a list of dictionaries")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_location = attendee.get("event_location") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        message = template
        message = message.replace("{name}", name)
        message = message.replace("{event_title}", event_title)
        message = message.replace("{event_location}", event_location)
        message = message.replace("{event_date}", event_date)

        with open(f"output_{index}.txt", "w") as file:
            file.write(message)
