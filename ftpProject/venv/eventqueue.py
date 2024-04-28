import asyncio

class EventQueue(object): # Singleton definiton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(EventQueue, cls).__new__(cls)
        return cls.instance

    EventID = 1

    def __init__(self):
        self.Event = []


    def _clearEvents(self):
        """"Fully clears out the events effectively reseting the event Queue"""
        self.Event = []


    def getEvent(self): # Think about ways to return the event should events have ids?
        pass



    def appendEvent(self, info, eventID=None): # An event will have an ID and info that explains what it did.
        if eventID == None:
            eventID = EventQueue.EventID
            EventQueue.EventID += 1
        self.Event.append((info, eventID))










