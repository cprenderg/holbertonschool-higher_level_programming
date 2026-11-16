#!/usr/bin/env python3

template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""

attendees = [
	{"name": "Alice", "event_title": "Python Conference"},
	{"name": "Bob", "event_title": "Data Science Workshop"}
]

def generate_invitations(str: template, attendees):
	if isintance(template, str):
		if not template.strip():
			print("Template is empty, no output files generated.")
		else:
			for attendee in attendees:
				name = attendee["name"]
				event_title = attendee["event_title"]
				event_location = attendee["event_location"]
	else:
		print("Invalid format")
	
	if all(isinstance(item, dict) for item in attendees):
		if not attendees.strip():
			print("No data provided, no output files generated.")
	else:
		print("Invalid format")
