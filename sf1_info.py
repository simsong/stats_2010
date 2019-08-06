from copy import deepcopy
import math

# dimnames=[HHGQ, SEX, AGE, HISP, CENRACE, CITIZEN], 
# shape=(8, 2, 116, 2, 63, 2), 

default_HHGQ = range(8)
default_SEX = range(2)
default_AGE = range(116)
default_HISP = range(2)
default_CENRACE = range(63)
default_CITIZEN = range(2)

# This a dict with the number of proper variables for each Table this is to confirm we are getting the right number
# this is just to have a extra level of protection to make sure that we get all of the variabes.
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
    raise ValueError(f"No Builder found for table {table_name}")

class Builder:
    def __init__(self):
        print('Creating Builder')

    def create_map(self, variables):
        for index, variable in enumerate(variables):
            self.build_map(index, variable)
    
    def process_results(self, results, table_name):
        # print(self.map)
        # go through all the rows and see if any values are zero if they are
        # add a entry into the multi_index array
        to_return = []
        for row in results.collect():
            for key, value in self.map.items():
                if row[key] == 0:
                    current_array = deepcopy(self.map[key])
                    current_array.insert(0, [ row['STATE'] ])
                    to_return.append(current_array)
        print(f"Table Name: {table_name} Length to return: {len(to_return)}")
        return to_return

    def build_map(self, index, variable):
        pass


# I am not sure this is the best way to do this but I could not find anywhere else that mapped the data dict variables to 
# the 6-D array
class P3_Builder(Builder):

    def __init__(self, variables):
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

        self.bucket_ends = [4, 9, 14, 17, 19, 20, 21, 24, 29, 34, 39, 44, 49, 54, 59, 61, 64, 66, 69, 74, 79, 84, 116]
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
                copy_default[1] = key
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
        copy_default = deepcopy(self.default_P12)
        for key, value in self.range_map.items():
            if variable >= value[0] and variable <= value[1]:
                copy_default[1] = key
                if key == 0:
                    copy_default[2] = self.buckets[index]
                else:
                    copy_default[2] = self.buckets[index - 19]
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

# class P38_Builder(Builder):

#     def __init__(self, variables):
#         variable_map = {
#             "Male_Under_18" : [""]
#         }

#         default_P38_correctional = [[1], default_SEX, -1, default_HISP, default_CENRACE, default_CITIZEN]
#         default_P38_correctional =



# 1,3,4
# 5,6,7

default_HHGQ = range(8)
default_SEX = range(2)
default_AGE = range(116)
default_HISP = range(2)
default_CENRACE = range(63)
default_CITIZEN = range(2)




