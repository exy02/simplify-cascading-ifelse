#sample nested dictionary
nested_dict = {"part_1": lambda var: sample_func_1(var),
              "part_2": lambda var,num: sample_func_2(var,num),
              "part_3": {"component_1": lambda var: sample_func_1(var),
                         "component_2": lambda var,num: sample_func_2(var,num),
                         "component_3": {"sub_component_1": lambda var: sample_func_1(var),
                                         "sub_component_2": lambda var,num: sample_func_2(var,num)
                                        },
                        },
             }
