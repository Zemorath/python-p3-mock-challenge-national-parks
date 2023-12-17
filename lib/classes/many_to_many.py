import datetime
from operator import attrgetter

class NationalPark:

    all = []

    def __init__(self, name):
        self._name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and (len(name) >= 3):
            if self._name == name:
                self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        unique_list = []

        for trip in self.trips():
            if trip.visitor not in unique_list:
                unique_list.append(trip.visitor)

        return unique_list
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):

        a = []
        for trip in self.trips():
            a.append(trip.visitor)
        max_attr = max(a, key=a.count)
        return max_attr


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        date_format = '%B %-d'
        if (type(start_date) == str) and (len(start_date) >= 7):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if (type(end_date) == str) and (len(end_date) >= 7):
            self._end_date = end_date


class Visitor:

    all = []

    def __init__(self, name):
        self._name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name

        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        unique_list = []

        for trip in self.trips():
            if trip.national_park not in unique_list:
                unique_list.append(trip.national_park)
        
        return unique_list
    
    def total_visits_at_park(self, park):
        counter = 0

        for a in self.trips():
            if a.park == park:
                counter +=1
            else:
                pass
        return counter