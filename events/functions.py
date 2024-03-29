from .models import Event
import datetime

def get_updated_event_list():
    #get all events from today or higher
    try:
        events = Event.objects.filter(from_date__gte=datetime.date.today()).order_by("from_date")
    except OperationalError :
        events = []
    return events


