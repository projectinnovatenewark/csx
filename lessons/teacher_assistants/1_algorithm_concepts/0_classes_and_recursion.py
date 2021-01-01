class Place():
  def __init__(self, place_type, name):
    self.place_type = place_type
    self.name = name
    self.sub_place = None

  def print_places(self):
    print(f"The place is called {self.name}")
    if self.sub_place != None:
      self.sub_place.print_places()

place1 = Place("Country", "USA")

place2 = Place("State", "New Jersey")
place1.sub_place = place2

place1.print_places()
