from collections import OrderedDict
from string import ascii_uppercase
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

    def __init__(self):
        self.map = {
            "P015001": [default_HHSEX, default_HHAGE, default_HISP, default_RACE, default_SIZE, default_HHTYPE,
                        default_ELDERLY, default_MULTI]
        }
        super().__init__()


class P18_Builder(Builder_HouseHold):

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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


class P31_Letter_Builder(Builder_HouseHold):

    def __init__(self, table_name):
        self.P31_Default = [default_HHSEX, default_HHAGE, -1, -1, default_SIZE, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                            default_ELDERLY, default_MULTI]
        self.map = OrderedDict([])
        self.race_for_table = default_RACE
        self.hisp_for_table = default_HISP
        self.table_variable = None

        self.specific_P31_table(table_name)
        self.build_map()

    def build_table_variable_name(self, table_letter):
        return f'P031{table_letter}001'

    def specific_P31_table(self, table_name):
        if table_name == 'P31A':
            self.race_for_table = [0]
            self.table_variable = self.build_table_variable_name('A')
        elif table_name == 'P31B':
            self.race_for_table = [1]
            self.table_variable = self.build_table_variable_name('B')
        elif table_name == 'P31C':
            self.race_for_table = [3]
            self.table_variable = self.build_table_variable_name('C')
        elif table_name == 'P31D':
            self.race_for_table = [2]
            self.table_variable = self.build_table_variable_name('D')
        elif table_name == 'P31E':
            self.race_for_table = [4]
            self.table_variable = self.build_table_variable_name('E')
        elif table_name == 'P31F':
            self.race_for_table = [5]
            self.table_variable = self.build_table_variable_name('F')
        elif table_name == 'P31G':
            self.race_for_table = [6]
            self.table_variable = self.build_table_variable_name('G')
        elif table_name == 'P31H':
            self.hisp_for_table = [1]
            self.table_variable = self.build_table_variable_name('H')
        elif table_name == 'P31I':
            self.race_for_table = [0]
            self.hisp_for_table = [0]
            self.table_variable = self.build_table_variable_name('I')

    def build_map(self):
        current_default = deepcopy(self.P15_Default)
        current_default[2] = self.hisp_for_table
        current_default[3] = self.race_for_table
        self.map[self.table_variable] = current_default


class P15_Letter_Builder(Builder_HouseHold):

    def __init__(self, table_name):
        self.P15_Default = [default_HHSEX, default_HHAGE, -1, -1, default_SIZE, default_HHTYPE,
                              default_ELDERLY, default_MULTI]
        self.map = OrderedDict([])
        self.race_for_table = default_RACE
        self.hisp_for_table = default_HISP
        self.table_variable = None

        self.specific_P15_table(table_name)
        self.build_map()

    def build_table_variable_name(self, table_letter):
        return f'P015{table_letter}001'

    def specific_P15_table(self, table_name):
        if table_name == 'P15A':
            self.race_for_table = [0]
            self.table_variable = self.build_table_variable_name('A')
        elif table_name == 'P15B':
            self.race_for_table = [1]
            self.table_variable = self.build_table_variable_name('B')
        elif table_name == 'P15C':
            self.race_for_table = [3]
            self.table_variable = self.build_table_variable_name('C')
        elif table_name == 'P15D':
            self.race_for_table = [2]
            self.table_variable = self.build_table_variable_name('D')
        elif table_name == 'P15E':
            self.race_for_table = [4]
            self.table_variable = self.build_table_variable_name('E')
        elif table_name == 'P15F':
            self.race_for_table = [5]
            self.table_variable = self.build_table_variable_name('F')
        elif table_name == 'P15G':
            self.race_for_table = [6]
            self.table_variable = self.build_table_variable_name('G')
        elif table_name == 'P15H':
            self.hisp_for_table = [1]
            self.table_variable = self.build_table_variable_name('H')
        elif table_name == 'P15I':
            self.race_for_table = [0]
            self.hisp_for_table = [0]
            self.table_variable = self.build_table_variable_name('I')

    def build_map(self):
        current_default = deepcopy(self.P15_Default)
        current_default[2] = self.hisp_for_table
        current_default[3] = self.race_for_table
        self.map[self.table_variable] = current_default


class P26_Letter_Builder(Builder_HouseHold):

    def __init__(self, table_name):
        self.map = OrderedDict([])
        self.race_for_table = default_RACE
        self.hisp_for_table = default_HISP
        self.table_variable = None
        super().__init__()

        self.specific_P26_table(table_name)
        self.build_map()

    def specific_P26_table(self, table_name):
        if table_name == 'P26':
            self.table_variable = ''
        elif table_name == 'P26A':
            self.race_for_table = [0]
            self.table_variable = 'A'
        elif table_name == 'P26B':
            self.race_for_table = [1]
            self.table_variable = 'B'
        elif table_name == 'P26C':
            self.race_for_table = [3]
            self.table_variable = 'C'
        elif table_name == 'P26D':
            self.race_for_table = [2]
            self.table_variable = 'D'
        elif table_name == 'P26E':
            self.race_for_table = [4]
            self.table_variable = 'E'
        elif table_name == 'P26F':
            self.race_for_table = [5]
            self.table_variable = 'F'
        elif table_name == 'P26G':
            self.race_for_table = [6]
            self.table_variable = 'G'
        elif table_name == 'P26H':
            self.hisp_for_table = [1]
            self.table_variable = 'H'
        elif table_name == 'P26I':
            self.race_for_table = [0]
            self.hisp_for_table = [0]
            self.table_variable = 'I'

    def build_map(self):
        if self.table_variable is None:
            raise ValueError("P26 table letter did not get set.")
        self.map = OrderedDict(
            [
                (f"P026{self.table_variable}003", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [2],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI]),
                (f"P026{self.table_variable}004", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [3],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI]),
                (f"P026{self.table_variable}005", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [4],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI]),
                (f"P026{self.table_variable}006", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [5],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI]),
                (f"P026{self.table_variable}007", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [6],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI]),
                (f"P026{self.table_variable}008", [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, [7],
                                                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22],
                                                   default_ELDERLY, default_MULTI])
            ]
        )
        temp_map = {}
        repeat_variables = [f"P026{self.table_variable}010", f"P026{self.table_variable}011", f"P026{self.table_variable}012", f"P026{self.table_variable}013",
                            f"P026{self.table_variable}014", f"P026{self.table_variable}015", f"P026{self.table_variable}016"]
        non_family = [default_HHSEX, default_HHAGE, self.hisp_for_table, self.race_for_table, -1, [12, 17, 18, 23],
                      default_ELDERLY, default_MULTI]
        for index, variable in enumerate(repeat_variables):
            current_value = deepcopy(non_family)
            current_value[4] = [index + 1]
            temp_map[variable] = current_value
        self.map.update(temp_map)

# [default_HHSEX, default_HHAGE, default_HISP, default_RACE, default_SIZE, default_HHTYPE,
#                         default_ELDERLY, default_MULTI]
