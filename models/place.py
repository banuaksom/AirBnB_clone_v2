#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


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
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False
                                 ))
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 backref='place',
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Return list of Review instances with place_id equal to current
            Place.id
            """
            reviews = []
            for review in models.storage.all(Review).values:
                if self.id == review.place_id:
                    reviews.append(review)
                    return reviews

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the
            attribute amenity_ids
            """
            amenities = []
            for amenity in models.storage.all(Amenity).values:
                if self.id == amenity.place_id:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """setter that appends Amenity.id to the
            attribute amenity_ids
            """
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
