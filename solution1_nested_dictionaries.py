# ======================
#Part 1: The Problem
# ======================
#Complex cascading if/else statements can be quickly become difficult to update and maintain.
def stats_func_old(part, component, sub_component, var):
  if part == 'part_1':
    result = sample_func_1(var,'func1_param')
  elif part == 'part_2':
    result = sample_func_2(var,'func2_param')
  elif part == 'part_3':
    result = sample_func_3(var,'func3_param')
  elif part == 'part_4':
    if component == 'component_1':
      result = sample_func_4(var,'func4_param')
    elif component == 'component_2':
      result = sample_func_4(var,'func4_param')
    elif component == 'component_3':
      result = sample_func_1(var,'func1_param')
    elif component == 'component_4':
      if sub_component == 'sub_component_1':
        result = sample_func_1(var,'func1_param')
      elif sub_component == 'sub_component_2':
        result = sample_func_2(var,'func2_param')
      elif sub_component == 'sub_component_3':
        result = sample_func_4(var,'func4_param') 
  elif part == 'part_5':
    if sub_component == 'sub_component_4':
      result = sample_func_3(var,'func3_param')
    else:
      return None
  else:
    return None
  return result
     
  
  
#These sample functions serve as our test functions for calling a 
#function directly through a defined nested dictionary
def sample_func_1(var,func1_param):
    result = print(f"Sample function {func1_param} #1 ~{var}")
    return result
def sample_func_2(var,func2_param):
    result = print(f"Sample function {func2_param} #2 ~{var}")
    return result
def sample_func_3(var,func3_param):
    result = print(f"Sample function {func3_param} #3 ~{var}")
    return result
def sample_func_4(var,func4_param):
    result = print(f"Sample function {func4_param} #4 ~{var}")
    return result

#sample function parameters to confirm correct function is called
var = "STRING"
  
  
  
# ======================
#Part 2: Proposed Solution v1.0
# ======================
#sample nested dictionary
nested_dict = {'part_1': lambda var: sample_func_1(var,'func1_param'),
               'part_2': lambda var: sample_func_2(var,'func2_param'),
               'part_3': lambda var: sample_func_3(var,'func3_param'),
               'part_4': {'component_1': lambda var: sample_func_4(var,'func4_param'),
                          'component_2': lambda var: sample_func_4(var,'func4_param'),
                          'component_3': lambda var: sample_func_1(var,'func1_param'),
                          'component_4': {'sub_component_1': lambda var: sample_func_1(var,'func1_param'),
                                          'sub_component_2': lambda var: sample_func_2(var,'func2_param'),
                                          'sub_component_3': lambda var: sample_func_4(var,'func4_param')
                                         },
                        },
               'part_5': {None: {'sub_component_4': lambda var: sample_func_3(var,'func3_param')
                                },
                         }
              }

#Here we assume class attribute part is always defined, whereas component and sub_component may be None.
#The cascade is simplified to whether or not a class attribute exists, followed by the corresponding dictionary format to execute the correct function.
#The result is an organized dictionary that can be quickly edited, and a shorter cascading if/else statement.
def stats_func_new(part, component, sub_component):
  dynamic = [part==None, component==None, sub_component==None]
  if dynamic == [False,False,False]:
    result = nested_dict[part][component][sub_component](var)
  elif dynamic == [False,False,True]:
    result = nested_dict[part][component](var)
  elif dynamic == [False,True,True]:
    result = nested_dict[part](var)
  elif dynamic == [False,True,False]:
    result = nested_dict[part][None][sub_component](var)
  return result
