from .coordinates import Coordinates
from .utils import countrycodes

class Location:
    """
    A location in the world affected by the coronavirus.
    """

    def __init__(self, id, country, province, coordinates, confirmed, deaths, recovered):
        # General info.
        self.id = id
        self.country = country.strip()
        self.province = province.strip()
        self.coordinates = coordinates

        # Data.
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered


    @property
    def country_code(self):
        """
        Gets the alpha-2 code represention of the country. Returns 'XX' if none is found.
        """
        return (countrycodes.country_code(self.country) or countrycodes.default_code).upper()

    def serialize(self):
        """
        Serializes the location into a dict.
        """
        return {
            # General info.
            'id'          : self.id,
            'country'     : self.country, 
            'province'    : self.province,
            'country_code': self.country_code,

            # Coordinates.
            'coordinates': self.coordinates.serialize(),

            # Latest data.
            'latest': {
                'confirmed': self.confirmed.latest,
                'deaths'   : self.deaths.latest,
                'recovered': self.recovered.latest
            }
        }