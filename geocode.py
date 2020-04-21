class GeoCode:
    def __init__(self, state_code, county_code, tract_code, blk_code="", area_land=None):
        self.state_code = state_code
        self.county_code = county_code
        self.tract_code = tract_code
        self.blk_code = blk_code
        self.area_land = area_land
        self.area_land_percentage = None

    def __str__(self):
        return self.state_code + self.county_code + self.tract_code + self.blk_code

    def __hash__(self):
        return hash((self.state_code, self.county_code, self.tract_code, self.blk_code, self.area_land))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.state_code == other.state_code and self.county_code == other.county_code \
            and self.tract_code == other.tract_code and self.blk_code == other.blk_code \
            and self.area_land == self.area_land
