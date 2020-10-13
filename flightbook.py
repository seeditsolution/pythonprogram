
class Flight:

    """A flight with a particular passenger aircraft."""
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))
        self._number = number
        self._aircraft = aircraft
        
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _
                                  in rows]


    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:
    def __init__(self, registration, model, maxrows, maxseatperrow):
        self._registration = registration
        self._model = model
        self._maxrows =maxrows
        self._maxseatperrow = maxseatperrow

    def registration(self):
        return self._registration

    def model(self):
        return self._model


    def seating_plan(self):
        return (range(1, self._maxrows + 1), "ABCDEFGHJK"[:self._maxseatperrow])


class AirbusA319:
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Airbus A319"
    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boeing777:
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Boeing 777"
    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"

class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats) 


class AirbusA319:
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Airbus A319"
    def seating_plan(self):
        return range(1, 23), "ABCDEF"
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class Boeing777:
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Boeing 777"
    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)
    
class AirbusA319(Aircraft):
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Airbus A319"
    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boeing777(Aircraft):
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def model(self):
        return "Boeing 777"
    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"



class Aircraft:
    def __init__(self, registration):
        self._registration = registration
    def registration(self):
        return self._registration
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"
    def seating_plan(self):
        return range(1, 23), "ABCDEF"



class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"
    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"

class Flight:

    """A flight with a particular passenger aircraft."""
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code'{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number'{}'".format(number))
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()
    
    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
            Args:
                seat: A seat designator such as '12C' or '21F'.
                passenger: The passenger name.
            Raises:
                ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]    
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger
       

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.
            Args:
                seat: A seat designator such as 12F
            Returns:
                A tuple containing an integer,string for row and seat.
            """
        row_numbers, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.
        Args:
        from_seat: The existing seat designator for the
        passenger to be moved.
        to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        return sum( sum(1 for s in row.values() if s is None)
                    for row in self._seating if row is not None )

    
def make_flights():
    f = Flight("BA758", AirbusA319("VT-AAA"))
    f.allocate_seat('12A', 'Harry Potter')
    f.allocate_seat('15F', 'Hermione Granger')
    f.allocate_seat('15E', 'Ron Weasely')
    f.allocate_seat('1C', 'Draco Malfoy')
    f.allocate_seat('1D', 'Gregory Goyle')
    g = Flight("AF72", Boeing777("VT-AAB"))
    g.allocate_seat('55K', 'Sirius Black')
    g.allocate_seat('33G', 'Remus Lupin')
    g.allocate_seat('4B', 'James Potter')
    g.allocate_seat('4A', 'Lily Potter')
    return f, g
    




def make_flight():
    a = Flight("AI758", Aircraft("VT-AAA", "Airbus A319", maxrows=22, maxseatperrow=6))
    a.allocate_seat('12A', 'Harry')
    a.allocate_seat('15F', 'Hermione')
    a.allocate_seat('15E', 'Ron')
    a.allocate_seat('1C', 'Draco')
    a.allocate_seat('1D', 'Goyle')
    return a



    def allocate_seat(seat, passenger):
        """Allocate a seat to a passenger.
            Args:
                seat: A seat designator such as '12C' or '21F'.
                passenger: The passenger name.
            Raises:
                ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()
               
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        row_text = seat[:-1]    
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger
    



    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
        Args:
        seat: A seat designator such as '12C' or '21F'.
        passenger: The passenger name.
        Raises:
        ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger

