from icalendar import Calendar, Event
from datetime import datetime

# Parse .ics file into human-readable text format
# Original data from 
# http://conferences.oreilly.com/strata/hadoop-big-data-ny/public/schedule/personal
# Sorry PEP8

file = open('strata.ics', 'rb')
cal = Calendar.from_ical(file.read())

start_format = "%a %b %d %H:%M"
end_format = "%H:%M" #only hour needed for end time

for component in cal.walk('vevent'):
	print "Event:", component.get('summary')
	print "Description:", component.get('description')
	print "Location:", component.get('location')
	start = component.get('dtstart')
	end = component.get('dtend')
	print "Time:" , start.dt.strftime(start_format), "-", end.dt.strftime(end_format)
	print "--------"


