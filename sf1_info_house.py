

default_HHSEX = range(2)
default_HHAGE = range(9)
default_HISP = range(2)
default_RACE = range(7)
default_SIZE = range(8)
default_HHTYPE = range(24)
default_ELDERLY = range(4)
default_MULTI = range(2)

# dimnames=[HHSEX, HHAGE, HISP, RACE, SIZE, HHTYPE, ELDERLY, MULTI],
# shape=(2, 9, 2, 7, 8, 24, 4, 2), path=path).getSchema()

# P015001


def get_correct_house_builder(table_name, values):
    pass


class Builder_HouseHold:

    def __init__(self):
        print('Created Builder_HouseHold')


class P15_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = {
            "P015001": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, default_SIZE, default_HHTYPE,
                        default_ELDERLY, default_MULTI]
        }
        super().__init__()


class P18_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = {
            "P018003": [[0], default_HHAGE, default_HISP, default_RACE, [1], [18],
                        default_ELDERLY, [0]],
            "P018004": [[1], default_HHAGE, default_HISP, default_RACE, [1], [18],
                        default_ELDERLY, [0]],
            "P018008": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(3, 8), [0, 1, 2],
                        default_ELDERLY, default_MULTI],
            "P018009": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2, 8), [3],
                        default_ELDERLY, default_MULTI],
            "P018012": [[0], default_HHAGE, default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                        default_ELDERLY, default_MULTI],
            "P018013": [[0], default_HHAGE, default_HISP, default_RACE, range(2, 8), [22],
                        default_ELDERLY, default_MULTI],
            "P018015": [[1], default_HHAGE, default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                        default_ELDERLY, default_MULTI],
            "P018016": [[1], default_HHAGE, default_HISP, default_RACE, range(2, 8), [22],
                        default_ELDERLY, default_MULTI],
            "P018018": [[0], default_HHAGE, default_HISP, default_RACE, range(2, 8), [12, 17, 18, 23],
                        default_ELDERLY, [0]],
            "P018019": [[1], default_HHAGE, default_HISP, default_RACE, range(2, 8), [12, 17, 18, 23],
                        default_ELDERLY, [0]],
        }
        super().__init__()


class P19_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = {
            "P019004": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(3, 8), [0, 1, 2],
                        default_ELDERLY, default_MULTI],
            "P019006": [[0], default_HHAGE, default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                        default_ELDERLY, default_MULTI],
            "P019007": [[1], default_HHAGE, default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                        default_ELDERLY, default_MULTI],
            "P019009": [[0], default_HHAGE, default_HISP, default_RACE, range(2, 8), [12, 17, 23],
                        default_ELDERLY, [0]],
            "P019010": [[1], default_HHAGE, default_HISP, default_RACE, range(2, 8), [12, 17, 23],
                        default_ELDERLY, [0]],

            "P019013": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2, 8), [3, 7],
                        default_ELDERLY, default_MULTI],
            "P019015": [[0], default_HHAGE, default_HISP, default_RACE, range(1, 8), [18, 22, 23],
                        default_ELDERLY, default_MULTI],
            "P019016": [[1], default_HHAGE, default_HISP, default_RACE, range(1, 8), [18, 22, 23],
                        default_ELDERLY, default_MULTI],
            "P019018": [[0], default_HHAGE, default_HISP, default_RACE, range(1, 8), [12, 17, 23],
                        default_ELDERLY, [0]],
            "P019019": [[1], default_HHAGE, default_HISP, default_RACE, range(1, 8), [12, 17, 23],
                        default_ELDERLY, [0]],
        }
        super().__init__()
