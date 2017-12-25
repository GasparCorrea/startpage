from googleapi import get_credentials
import httplib2
from apiclient import discovery
import datetime

def get_events():
    calendar = list()
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    for event in events:
        when = event['start'].get('dateTime', event['start'].get('date'))
        yyyy,mm,dd = when.split("T")[0].split("-")
        date = dd+"/"+mm
        summary = event['summary']
        calendar.append((date+" "+summary))
    return calendar