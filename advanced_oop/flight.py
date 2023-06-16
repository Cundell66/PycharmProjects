class Flight:
    def __init__(self, segments):
        self.segments = segments

    def __repr__(self):
        # return f'{self.segments[0].departure} --> {self.segments[0].destination} --> {self.segments[1].destination} '
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '-->'.join(stops)

    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, val):
        self.segments[0].departure = val


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


flight = Flight([Segment('GLA', 'LHR'), Segment('LHR', 'TOR')])

print(flight)

flight.departure_point = 'EDI'
print(flight)
