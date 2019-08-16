from collections import OrderedDict
from copy import deepcopy

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


class P20_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = OrderedDict(
            [
                ("P020005", [default_HHSEX, range(0, 6), default_HISP, default_RACE, range(3, 8), [0, 1, 2],
                             default_ELDERLY, default_MULTI]),
                ("P020006", [default_HHSEX, range(0, 6), default_HISP, default_RACE, range(2, 8), [3],
                             default_ELDERLY, default_MULTI]),
                ("P020009", [[0], range(0, 6), default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                             default_ELDERLY, default_MULTI]),
                ("P020010", [[0], range(0, 6), default_HISP, default_RACE, range(2, 8), [22],
                             default_ELDERLY, default_MULTI]),
                ("P020012", [[1], range(0, 6), default_HISP, default_RACE, range(2, 8), [19, 20, 21],
                             default_ELDERLY, default_MULTI]),
                ("P020013", [[1], range(0, 6), default_HISP, default_RACE, range(2, 8), [22],
                             default_ELDERLY, default_MULTI]),
                ("P020015", [default_HHSEX, range(0, 6), default_HISP, default_RACE, [1], [18],
                             default_ELDERLY, default_MULTI]),
                ("P020016", [default_HHSEX, range(0, 6), default_HISP, default_RACE, range(2, 8), [23],
                             default_ELDERLY, default_MULTI])
            ]
        )
        # The reason we are doing this is because the next 8 are the same as the first 8 just a different
        # value for the HHAGE. So we use a ordered dict so we can safely loop through the items
        # and add them back when the changes variable with a new key.
        temp_map = {}
        repeat_variables = ["P020020", "P020021", "P020024", "P020025", "P020027", "P020028", "P020030",
                            "P020031"]
        for index, (key, value) in enumerate(self.map.items()):
            current_value = deepcopy(value)
            current_value[1] = [6, 7, 8]
            temp_map[repeat_variables[index]] = current_value
        self.map.update(temp_map)
        super().__init__()

class P21_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = OrderedDict(
            [
                ("P021003", [default_HHSEX, [0], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021004", [default_HHSEX, [1], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021005", [default_HHSEX, [2], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021006", [default_HHSEX, [3], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021007", [default_HHSEX, [4, 5], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021008", [default_HHSEX, [6], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021009", [default_HHSEX, [7], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI]),
                ("P021010", [default_HHSEX, [8], default_HISP, default_RACE, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             default_ELDERLY, default_MULTI])
            ]
        )
        # The reason we are doing this is because the next 8 are the same as the first 8 just a different
        # value for the HHAGE. So we use a ordered dict so we can safely loop through the items
        # and add them back when the changes variable with a new key.
        temp_map = {}
        repeat_variables = ["P021012", "P021013", "P021014", "P021015", "P021016", "P021017", "P021018",
                            "P021019"]
        for index, (key, value) in enumerate(self.map.items()):
            current_value = deepcopy(value)
            current_value[5] = [12, 17, 18, 23]
            temp_map[repeat_variables[index]] = current_value
        self.map.update(temp_map)
        super().__init__()

class P22_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = OrderedDict(
            [
                ("P022003", [default_HHSEX, [5, 6, 7, 8], default_HISP, default_RACE, [1], [18],
                             [1, 2, 3], [0]]),
                ("P022005", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             [1, 2, 3], default_MULTI]),
                ("P022006", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [12, 17, 23],
                             [1, 2, 3], [0]])
            ]
        )
        temp_map = {}
        repeat_variables = ["P022008", "P022010", "P022011"]
        for index, (key, value) in enumerate(self.map.items()):
            current_value = deepcopy(value)
            current_value[1] = [0, 1, 2, 3, 4]
            current_value[6] = [0]
            temp_map[repeat_variables[index]] = current_value
        self.map.update(temp_map)
        super().__init__()

class P23_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = OrderedDict(
            [
                ("P023003", [default_HHSEX, [6, 7, 8], default_HISP, default_RACE, [1], [18],
                             [2, 3], [0]]),
                ("P023005", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             [2, 3], default_MULTI]),
                ("P023006", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [12, 17, 23],
                             [2, 3], [0]])
            ]
        )
        temp_map = {}
        repeat_variables = ["P023008", "P023010", "P023011"]
        for index, (key, value) in enumerate(self.map.items()):
            current_value = deepcopy(value)
            current_value[1] = [0, 1, 2, 3, 4, 5]
            current_value[6] = [0, 1]
            temp_map[repeat_variables[index]] = current_value
        self.map.update(temp_map)
        super().__init__()

class P24_Builder(Builder_HouseHold):

    def __init__(self, variables):
        self.map = OrderedDict(
            [
                ("P024003", [default_HHSEX, [7, 8], default_HISP, default_RACE, [1], [18],
                             [2, 3], [0]]),
                ("P024005", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                             [2, 3], default_MULTI]),
                ("P024006", [default_HHSEX, default_HHAGE, default_HISP, default_RACE, range(2,8), [12, 17, 23],
                             [2, 3], [0]])
            ]
        )
        temp_map = {}
        repeat_variables = ["P024008", "P024010", "P024011"]
        for index, (key, value) in enumerate(self.map.items()):
            current_value = deepcopy(value)
            current_value[1] = [0, 1, 2, 3, 4, 5, 6]
            current_value[6] = [0, 1, 2]
            temp_map[repeat_variables[index]] = current_value
        self.map.update(temp_map)
        super().__init__()

class P25_Builder(Builder_HouseHold):

    def __init__(self, variables):
        pass