from copy import deepcopy

# dimnames=[HHGQ, SEX, AGE, HISP, CENRACE, CITIZEN], 
# shape=(8, 2, 116, 2, 63, 2), 

default_HHGQ = range(8)
default_SEX = range(2)
default_AGE = range(116)
default_HISP = range(2)
default_CENRACE = range(63)
default_CITIZEN = range(2)


def get_correct_builder(table_name, values):
    if table_name == "P3":
        return P3_Builder(values)
    elif table_name == "P4":
        return P4_Builder(values)
    elif table_name == "P5":
        return P5_Builder(values)

class Builder:
    def __init__(self):
        self.variables = []
        self.build_variables()
    
    def process_results(self, results, current_var):
        print(self.map)
        to_return = []
        for row in results.collect():
            current_array = deepcopy(self.map[current_var])
            current_array.insert(0, row['STATE'])
            to_return.append(current_array)
        return to_return

    def build_variables():
        pass


# I am not sure this is the best way to do this but I could not find anywhere else that mapped the data dict variables to 
# the 6-D array
class P3_Builder(Builder):

    def __init__(self, values):
        super.__init__()
        default_P3 = [default_HHGQ, default_SEX, default_AGE, default_HISP, -1, default_CITIZEN]
        self.map = {}
        for index, value in enumerate(values):
            copy_default = deepcopy(default_P3)
            copy_default[4] = index
            self.map[value] = copy_default

    # The sf1 parser is missing some of the variables.
    # Should possibly fix the parser but just wanted to see if this would work
    def build_variables(self):
        variable_format = "P003000"
        for i in range(1, 72):
            if len(str(i)) == 1:
                self.variables.append(variable_format[-1:] + str(i))
            elif len(str(i)) == 2:
                self.variables.append(variable_format[-2:] + str(i))
    
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
