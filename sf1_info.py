from copy import deepcopy
import math
from functools import reduce
from string import ascii_uppercase

default_HHGQ = range(8)
default_SEX = range(2)
default_AGE = range(116)
default_HISP = range(2)
default_CENRACE = range(63)
default_CITIZEN = range(2)

default_hist = [default_HHGQ, default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN]

# This a dict with the number of proper variables for each Table this is to confirm we are getting the right number
# this is just to have a extra level of protection to make sure that we get all of the variabes.

table_size = {
    "P3": 70,
    "P4": 72,
    "P5": 71,
    "P6": 72,
    "P12": 48
}


def get_correct_builder(table_name, values):
    p12_letter_tables = [f"P12{letter}" for letter in ascii_uppercase[:9]]
    pct12_letter_tables = ['PCT12']
    pct12_letter_tables += [f"PCT12{letter}" for letter in ascii_uppercase[:15]]
    pct13_letter_tables = ['PCT13']
    pct13_letter_tables += [f"PCT13{letter}" for letter in ascii_uppercase[:12]]
    if table_name == "P3":
        return P3_Builder(values)
    elif table_name == "P4":
        return P4_Builder(values)
    elif table_name == "P5":
        return P5_Builder(values)
    elif table_name == "P6":
        return P6_Builder(values)
    elif table_name == "P12":
        return P12_Builder(values)
    elif table_name == "P14":
        return P14_Builder(values)
    elif table_name == "P16":
        return P16_Builder(values)
    elif table_name == "P37":
        return P37_Builder(values)
    elif table_name in p12_letter_tables:
        return P12_Letter_Builder(values, table_name)
    elif table_name in pct12_letter_tables:
        return PCT12_Builder(values, table_name)
    elif table_name in pct13_letter_tables:
        return PCT13_Builder(values, table_name)
    raise ValueError(f"No Builder found for table {table_name}")


class Histogram:
    def __init__(self, row, summary_level, histogram):
        self.geo_code_parts = {}
        self.full_geo_code = ""
        self.histogram = histogram
        self.create_geocode(row, summary_level)
        self.histogram_expanded = None

        self.histogram.insert(0, [self.full_geo_code])

    def generate_expanded_histogram(self):
        self.histogram_expanded = Histogram.cartesian_iterative(self.histogram)

    def create_geocode(self, row, summary_level):
        geo_levels = ['STATE', 'COUNTY', 'TRACT']
        index = geo_levels.index(summary_level) + 1
        for element in geo_levels[:index]:
            self.geo_code_parts[element] = row[element]
            self.full_geo_code += row[element]

    def __str__(self):
        return str(self.histogram) if not self.histogram_expanded else str(self.histogram_expanded)

    @staticmethod
    def cartesian_iterative(pools):
        result = [()]
        for pool in pools:
            result = [x + (y,) for x in result for y in pool]
        return result


class Builder:
    def __init__(self):
        print('Creating Builder')

    def create_map(self, variables):
        for index, variable in enumerate(variables):
            self.build_map(index, variable)

    def process_results(self, summary_level, results, table_name, cell_size_num):
        to_return = []
        for row in results.collect():
            for key, value in self.map.items():
                average_contained_cell_size = self.compute_average_contained_cell_size(row[key], self.map[key])
                if average_contained_cell_size <= cell_size_num:
                    current_histogram = Histogram(row, summary_level, deepcopy(self.map[key]))
                    to_return.append(current_histogram)
        print(f"Table Name: {table_name} Length to return: {len(to_return)}")
        return to_return

    def compute_average_contained_cell_size(self, count, cell_array):
        try:
            cell_array_lengths = [len(current) for current in cell_array]
            result = reduce((lambda x, y: x * y), cell_array_lengths)
            return count / result
        except Exception:
            print(cell_array)
            raise ValueError('Could not convert this array.')

    def build_map(self, index, variable):
        pass


# I am not sure this is the best way to do this but I could not find anywhere else that mapped the data dict variables to 
# the 6-D array
class P3_Builder(Builder):

    def __init__(self, variables):
        self.insert_locations = [4]
        self.default_P3 = [default_HHGQ, default_SEX, default_AGE, default_HISP, -1, default_CITIZEN]
        self.map = {}
        super().__init__()
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P3)
        copy_default[4] = [index]
        self.map[variable] = copy_default

    
class P4_Builder(Builder):

    def __init__(self, variables):
        super().__init__()
        self.hispanic_P4 = [default_HHGQ, default_SEX, default_AGE, [1], default_CENRACE, default_CITIZEN]
        self.non_hispanic_P4 = [default_HHGQ, default_SEX, default_AGE, [0], -1, default_CITIZEN]

        try:
            variables.remove("P004002")
        except ValueError:
            raise ValueError("Did not find P004002 in the P4 variables list this is bad")
        self.map = {
            "P004002": self.hispanic_P4
        }
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.non_hispanic_P4)
        copy_default[4] = [index]
        self.map[variable] = copy_default

class P5_Builder(Builder):

    def __init__(self, variables):
        super().__init__()
        self.default_P5 = [default_HHGQ, default_SEX, range(18, 116), default_HISP, -1, default_CITIZEN]
        self.map = {}
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P5)
        copy_default[4] = [index]
        self.map[variable] = copy_default

class P6_Builder(Builder):

    def __init__(self, variables):
        super().__init__()
        self.hispanic_P6 = [default_HHGQ, default_SEX, range(18, 116), [1], default_CENRACE, default_CITIZEN]
        self.non_hispanic_P6 = [default_HHGQ, default_SEX, range(18, 116), [0], -1, default_CITIZEN]

        try:
            variables.remove("P006002")
        except ValueError:
            raise ValueError("Did not find P006002 in the P4 variables list this is bad")
        self.map = {
            "P006002": self.hispanic_P6
        }
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.non_hispanic_P6)
        copy_default[4] = [index]
        self.map[variable] = copy_default

class P12_Builder(Builder):
    
    def __init__(self, variables):
        super().__init__()
        self.default_P12 = [default_HHGQ, -1, -1, default_HISP, default_CENRACE, default_CITIZEN]
        self.map = {}

        self.range_map = {
            0: ['P012003', 'P012025'],
            1: ['P012027', 'P012049']
        }

        self.bucket_ends = [4, 9, 14, 17, 19, 20, 21, 24, 29, 34, 39, 44, 49, 54, 59, 61, 64, 66, 69, 74, 79, 84, 115]
        self.buckets = []

        for i in range(len(self.bucket_ends)):
            if i == 0:
                self.buckets.append(range(self.bucket_ends[i] + 1))
            else:
                self.buckets.append(range(self.bucket_ends[i - 1] + 1, self.bucket_ends[i] + 1))
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P12)
        for key, value in self.range_map.items():
            if variable >= value[0] and variable <= value[1]:
                copy_default[1] = [key]
                if key == 0:
                    copy_default[2] = self.buckets[index]
                else:
                    copy_default[2] = self.buckets[index - len(self.bucket_ends)]
        self.map[variable] = copy_default

class P14_Builder(Builder):

    def __init__(self, variables):
        super().__init__()
        self.default_P14 = [default_HHGQ, -1, -1, default_HISP, default_CENRACE, default_CITIZEN]
        self.map = {}
        self.range_map = {
            0: ['P014003', 'P014022'],
            1: ['P014024', 'P014043']
        }
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P14)
        for key, value in self.range_map.items():
            if variable >= value[0] and variable <= value[1]:
                copy_default[1] = [key]
                if key == 0:
                    copy_default[2] = [index]
                else:
                    copy_default[2] = [index - 19]
        self.map[variable] = copy_default

class P16_Builder(Builder):

    def __init__(self, variables):
        super().__init__()

        self.default_P16 = [default_HHGQ, default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN]
        self.map = {}
        
        self.create_map(variables)

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P16)
        self.map[variable] = copy_default

class P37_Builder(Builder):

    def __init__(self, variables):
        super().__init__()
        # Did not know a better way to map this. So since it was a small amount of variables just enumerated by hand.
        self.map = {
            "P037003": [[1], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN],
            "P037004": [[3], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN],
            "P037005": [[4], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN],
            "P037007": [[5], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN],
            "P037008": [[6], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN],
            "P037009": [[7], default_SEX, default_AGE, default_HISP, default_CENRACE, default_CITIZEN]
        }
        self.create_map(variables)

class P12_Letter_Builder(Builder):

    def __init__(self, variables, table_name):
        super().__init__()
        self.default_P12 = [default_HHGQ, -1, -1, default_HISP, default_CENRACE, default_CITIZEN]
        self.map = {}
        # The next two variables are filled in using the function specific_P12_table.
        self.default_CENRACE_for_table = None
        self.is_hispanic = None

        # A tables in this group has the same age buckets.
        self.bucket_ends = [4, 9, 14, 17, 19, 20, 21, 24, 29, 34, 39, 44, 49, 54, 59, 61, 64, 66, 69, 74, 79, 84, 115]
        self.buckets = []

        for i in range(len(self.bucket_ends)):
            if i == 0:
                self.buckets.append(range(self.bucket_ends[i] + 1))
            else:
                self.buckets.append(range(self.bucket_ends[i - 1] + 1, self.bucket_ends[i] + 1))
        # There should be double the buckets this is because there is males and females.
        self.buckets = self.buckets + self.buckets
        self.specific_P12_table(table_name)
        self.create_map(variables)

    # All of this group of tables follows the same pattern for naming there variable names.
    def build_range_map(self, table_letter):
        self.range_map = {
            0: [f'P012{table_letter}003', f'P012{table_letter}025'],
            1: [f'P012{table_letter}027', f'P012{table_letter}049']
        }

    # This class is going to handle all of the P12Letter Tables.
    # So this function is just to put any specific needed logic.
    def specific_P12_table(self, table_name):
        if table_name == "P12A":
            self.build_range_map('A')
            self.default_CENRACE_for_table = [0]
        elif table_name == "P12B":
            self.build_range_map('B')
            self.default_CENRACE_for_table = [1]
        elif table_name == "P12C":
            self.build_range_map('C')
            self.default_CENRACE_for_table = [2]
        elif table_name == "P12D":
            self.build_range_map('D')
            self.default_CENRACE_for_table = [3]
        elif table_name == "P12E":
            self.build_range_map('E')
            self.default_CENRACE_for_table = [4]
        elif table_name == "P12F":
            self.build_range_map('F')
            self.default_CENRACE_for_table = [5]
        elif table_name == "P12G":
            self.build_range_map('G')
            self.default_CENRACE_for_table = list(range(6, 21))
        elif table_name == "P12H":
            self.build_range_map('H')
            self.is_hispanic = [1]
        elif table_name == "P12I":
            self.build_range_map('I')
            self.is_hispanic = [0]
            self.default_CENRACE_for_table = [0]

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_P12)
        for key, value in self.range_map.items():
            if variable >= value[0] and variable <= value[1]:
                copy_default[1] = [key]
                copy_default[2] = self.buckets[index]
                if self.default_CENRACE_for_table is not None:
                    copy_default[4] = self.default_CENRACE_for_table
                if self.is_hispanic is not None:
                    copy_default[3] = self.is_hispanic
        self.map[variable] = copy_default


class PCT12_Builder(Builder):

    def __init__(self, variables, table_name):
        super().__init__()
        self.default_PCT12 = [default_HHGQ, -1, -1, -1, -1, default_CITIZEN]
        self.range_map = {}
        self.map = {}
        self.default_CENRACE_for_table = default_CENRACE
        self.default_HISP_for_table = default_HISP

        self.non_processed_buckets = list(range(100)) + [list(range(100, 105)), list(range(105, 110)), list(range(110, 116))]
        self.buckets = [[loop] if isinstance(loop, int) else loop for loop in self.non_processed_buckets]
        # This is because we have buckets for male and female.
        self.buckets += self.buckets
        self.specific_PCT12_table(table_name)
        self.create_map(variables)

    def build_range_map(self, table_letter):
        self.range_map = {
            0: [f'PCT012{table_letter}003', f'PCT012{table_letter}105'],
            1: [f'PCT012{table_letter}107', f'PCT012{table_letter}209']
        }

    def specific_PCT12_table(self, table_name):
        if table_name == "PCT12":
            self.build_range_map('')
        elif table_name == "PCT12A":
            self.build_range_map('A')
            self.default_CENRACE_for_table = [0]
        elif table_name == "PCT12B":
            self.build_range_map('B')
            self.default_CENRACE_for_table = [1]
        elif table_name == "PCT12C":
            self.build_range_map('C')
            self.default_CENRACE_for_table = [2]
        elif table_name == "PCT12D":
            self.build_range_map('D')
            self.default_CENRACE_for_table = [3]
        elif table_name == "PCT12E":
            self.build_range_map('E')
            self.default_CENRACE_for_table = [4]
        elif table_name == "PCT12F":
            self.build_range_map('F')
            self.default_CENRACE_for_table = [5]
        elif table_name == "PCT12G":
            self.build_range_map('G')
            self.default_CENRACE_for_table = list(range(6, 21))
        elif table_name == "PCT12H":
            self.build_range_map('H')
            self.default_HISP_for_table = [1]
        elif table_name == "PCT12I":
            self.build_range_map('I')
            self.default_CENRACE_for_table = [0]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12J":
            self.build_range_map('J')
            self.default_CENRACE_for_table = [1]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12K":
            self.build_range_map('K')
            self.default_CENRACE_for_table = [2]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12L":
            self.build_range_map('L')
            self.default_CENRACE_for_table = [3]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12M":
            self.build_range_map('M')
            self.default_CENRACE_for_table = [4]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12N":
            self.build_range_map('N')
            self.default_CENRACE_for_table = [5]
            self.default_HISP_for_table = [0]
        elif table_name == "PCT12O":
            self.build_range_map('O')
            self.default_CENRACE_for_table = list(range(6, 21))
            self.default_HISP_for_table = [0]
        else:
            raise ValueError(f'Failed to find {table_name} in PCT12_Builder.')

    def build_map(self, index, variable):
        copy_default = deepcopy(self.default_PCT12)
        for key, value in self.range_map.items():
            if value[0] <= variable <= value[1]:
                copy_default[1] = [key]
                copy_default[2] = self.buckets[index]
                if self.default_HISP_for_table:
                    copy_default[3] = self.default_HISP_for_table
                if self.default_CENRACE_for_table:
                    copy_default[4] = self.default_CENRACE_for_table
        self.map[variable] = copy_default


class PCT13_Builder(Builder):

        def __init__(self, variables, table_name):
            super().__init__()
            self.default_PCT13 = [default_HHGQ, -1, -1, -1, -1, default_CITIZEN]
            self.map = {}
            self.range_map = {}

            self.default_CENRACE_for_table = default_CENRACE
            self.default_HISP_for_table = default_HISP

            self.bucket_ends = [4, 9, 14, 17, 19, 20, 21, 24, 29, 34, 39, 44, 49, 54, 59, 61, 64, 66, 69, 74, 79, 84, 115]
            self.buckets = []

            for i in range(len(self.bucket_ends)):
                if i == 0:
                    self.buckets.append(range(self.bucket_ends[i] + 1))
                else:
                    self.buckets.append(range(self.bucket_ends[i - 1] + 1, self.bucket_ends[i] + 1))
            self.buckets += self.buckets
            self.specific_PCT13_table(table_name)
            self.create_map(variables)

        def build_range_map(self, table_letter):
            self.range_map = {
                0: [f'PCT013{table_letter}003', f'PCT013{table_letter}025'],
                1: [f'PCT013{table_letter}027', f'PCT013{table_letter}049']
            }

        def specific_PCT13_table(self, table_name):
            if table_name == "PCT13":
                self.build_range_map('')
            elif table_name == "PCT13A":
                self.build_range_map('A')
                self.default_CENRACE_for_table = [0]
            elif table_name == "PCT13B":
                self.build_range_map('B')
                self.default_CENRACE_for_table = [1]
            elif table_name == "PCT13C":
                self.build_range_map('C')
                self.default_CENRACE_for_table = [2]
            elif table_name == "PCT13D":
                self.build_range_map('D')
                self.default_CENRACE_for_table = [3]
            elif table_name == "PCT13E":
                self.build_range_map('E')
                self.default_CENRACE_for_table = [4]
            elif table_name == "PCT13F":
                self.build_range_map('F')
                self.default_CENRACE_for_table = [5]
            elif table_name == "PCT13G":
                self.build_range_map('G')
                self.default_CENRACE_for_table = list(range(6, 21))
            elif table_name == "PCT13H":
                self.build_range_map('H')
                self.default_HISP_for_table = [1]
            elif table_name == "PCT13I":
                self.build_range_map('I')
                self.default_CENRACE_for_table = [0]
                self.default_HISP_for_table = [0]
            else:
                raise ValueError(f'Failed to find {table_name} in PCT13_Builder.')

        def build_map(self, index, variable):
            copy_default = deepcopy(self.default_PCT13)
            for key, value in self.range_map.items():
                if value[0] <= variable <= value[1]:
                    copy_default[1] = [key]
                    copy_default[2] = self.buckets[index]
                    if self.default_HISP_for_table:
                        copy_default[3] = self.default_HISP_for_table
                    if self.default_CENRACE_for_table:
                        copy_default[4] = self.default_CENRACE_for_table
            self.map[variable] = copy_default
