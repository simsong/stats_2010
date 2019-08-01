from copy import deepcopy

# dimnames=[HHGQ, SEX, AGE, HISP, CENRACE, CITIZEN], 
# shape=(8, 2, 116, 2, 63, 2), 

default_HHGQ = range(8)
default_SEX = range(2)
default_AGE = range(116)
default_HISP = range(2)
default_CENRACE = range(63)
default_CITIZEN = range(2)

# This a dict with the number of proper variables for each Table this is to confirm we are getting the right number
# I have found that the CSV is not properly formed and is missing variables
geo_table_header_size = 6

table_size = {
    "P3": 70 + geo_table_header_size,
    "P4": 72 + geo_table_header_size,
    "P5": 71 + geo_table_header_size,
    "P6": 72 + geo_table_header_size,
    "P12": 48 + geo_table_header_size
}


def get_correct_builder(table_name, values):
    if table_name == "P3":
        return P3_Builder(values)
    elif table_name == "P4":
        return P4_Builder(values)
    elif table_name == "P5":
        return P5_Builder(values)

class Builder:
    def __init__(self):
        pass
    
    def process_results(self, results, table_name):
        print(self.map)
        # go through all the rows and see if any values are zero if they are
        # add a entry into the multi_index array
        to_return = []
        for row in results.collect():
            for key, value in self.map.items():
                if row[key] == 0:
                    current_array = deepcopy(self.map[key])
                    current_array.insert(0, row['STATE'])
                    to_return.append(current_array)
        print(f"Table Name: {table_name} Length to return: {len(to_return)}")
        return to_return


# I am not sure this is the best way to do this but I could not find anywhere else that mapped the data dict variables to 
# the 6-D array
class P3_Builder(Builder):

    def __init__(self, values):
        default_P3 = [default_HHGQ, default_SEX, default_AGE, default_HISP, -1, default_CITIZEN]
        self.map = {}
        for index, value in enumerate(values):
            copy_default = deepcopy(default_P3)
            copy_default[4] = index
            self.map[value] = copy_default
    
class P4_Builder(Builder):

    def __init__(self, values):
        hispanic_P4 = [default_HHGQ, default_SEX, default_AGE, 1, default_CENRACE, default_CITIZEN]
        non_hispanic_P4 = [default_HHGQ, default_SEX, default_AGE, 0, -1, default_CITIZEN]

        try:
            values.remove("P004002")
        except ValueError:
            print("Did not find P004002 in the P4 values list this is bad")
            raise ValueError
        self.map = {
            "P004002": hispanic_P4
        }
        for index, value in enumerate(values):
            copy_default = deepcopy(non_hispanic_P4)
            copy_default[4] = index
            self.map[value] = copy_default

class P5_Builder(Builder):

    def __init__(self, values):
        default_P5 = [default_HHGQ, default_SEX, range(18, 116), default_HISP, -1, default_CITIZEN]
        self.map = {}
        for index, value in enumerate(values):
            copy_default = deepcopy(default_P5)
            copy_default[4] = index
            self.map[value] = copy_default
