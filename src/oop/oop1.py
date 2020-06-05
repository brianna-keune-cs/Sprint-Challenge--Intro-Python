# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:  # parent/base class
    pass


class FlightVehicle(Vehicle):  # child of vehicle
    pass


class Starship(FlightVehicle):  # child of flight vehicle
    pass


class Airplane(FlightVehicle):  # child of flight vehicle
    pass


class GroundVehicle(Vehicle):  # child of vehicle
    pass


class Car(GroundVehicle):  # child of ground vehicle
    pass


class Motorcycle(GroundVehicle):  # child of ground vehicle
    pass
