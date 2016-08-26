'''
Python Version: 2.7
Parse .ics file into human-readable text format
Original data from 
http://conferences.oreilly.com/strata/hadoop-big-data-ny/public/schedule/personal
Sorry PEP8
'''

from icalendar import Calendar, Event
from datetime import datetime


# date formats for DTSTART and END
start_format = "%a %b %d %H:%M"
end_format = "%H:%M" #only hour needed for end time


def parse_ics(infile):
	
	cal = Calendar.from_ical(infile.read())

	events = []

	for component in cal.walk('vevent'):
		event =   component.get('summary')
		description =  component.get('description')
		location =  component.get('location')
		start = component.get('dtstart')
		end = component.get('dtend')
		total_time =  "%s-%s" % (start.dt.strftime(start_format) , end.dt.strftime(end_format))
		line =  "Summary:%s \nDescription: %s \nLocation: %s \nTime: %s \n------\n " % (event, description, location, total_time)
		events.append(line)

	return events

def ics_to_file(filename, events):
	with open(filename, 'w') as f:
		for e in events:
			f.write(e)


if __name__ == '__main__':
	infile = open('strata.ics', 'rb') #TODO: offer command line input as next step
	parsed_results = parse_ics(infile)
	ics_to_file('strata_2016_cal.txt', parsed_results)