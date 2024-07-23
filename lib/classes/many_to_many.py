class Band:
    all = []

    def __init__(self, name, hometown):
        self.name = name
        if isinstance(hometown, str) and len(hometown) > 0:
           self._hometown = hometown
        else: 
            raise Exception
        Band.all.append(self)
        self._concerts = []
        self._venues = set()

        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception
        
    @property
    def hometown(self):
        return self._hometown
    
    def concerts(self):
        return self._concerts
    
    def add_concert(self, concert):
        if isinstance(concert, Concert ) and concert.band == self:
            self._concerts.append(concert)
        else:
            raise ValueError

    def venues(self):
        return list({concert.venue for concert in self._concerts})
    
    def add_venue(self, venue):
        if isinstance(venue, Venue):
            self._venues.add(venue)
        else:
            raise ValueError

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        if concert not in self._concerts:
            self.add_concert(concert)
        if venue not in self._venues:
            self.add_venue(venue)
        venue.add_band(self)
        return concert
    
    def all_introductions(self):
        if not self._concerts:
            return None
        introductions = [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]
        return introductions

class Concert:
    all =[]


    def __init__(self, date, band, venue):
        if isinstance(band, Band) and isinstance(venue, Venue):
            self.band = band
            self.venue = venue
            self.date = date
            band.add_concert(self)
            venue.add_band(band)
            Concert.all.append(self)
        else:
            raise ValueError

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise Exception

    def hometown_show(self):
        return self.venue.city == self.band.hometown 

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._bands = set()
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) > 0:
            return Exception
        self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not isinstance(value, str) and len(value) > 0:
            return Exception
        self._city = value

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return list(self._bands)

    def add_band(self, band):
        if isinstance(band, Band):
            self._bands.add(band)
        else:
            raise ValueError
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
            else:
                return None
    
