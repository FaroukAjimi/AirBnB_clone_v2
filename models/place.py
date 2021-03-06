#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column("place_id",
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id",
                                 String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))
    
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref="places")
    amenities = relationship("Amenity", backref="place",
                             secondary="place_amenity", viewonly=False)

    #@property
    #def reviews(self):
    #    """
    #    """
    #    dictt = {}
    #    rev = models.storage.all(Review)
    #    for k, v in rev:
    #        if value.id == self.id:
    #            dictt[key] = value
    #    return (dictt)

    #@property
    #def amenities(self):
    #    """
    #    """
    #    dictt = {}
    #    rev = models.storage.all(Amenity)
    #    for k, v in rev:
    #        if value.id == self.id:
    #            dictt[key] = value
    #    return (dictt)

    #@amenities.setter
    #def amenities(self, obj):
    #    if obj.__class__.__name__ == "Amenity":
    #        self.amenity_id.append(str(obj.id))
