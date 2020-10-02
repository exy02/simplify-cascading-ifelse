#TODO: add sample
# Table query is dependent on database, and in this example we leverage a static dictionary to execute our functions (to avoid security holes via function injects).

dynamic = [component_type==None, sub_component==None, title==None]
if dynamic == [False,False,False]:
    result = Table.objects.filter(
        component_type__exact = f'{component_type}',
        sub_component_type__exact = f'{sub_component}',
        title__exact = f'{title}')
elif dynamic == [False,False,True]:
    result = Table.objects.filter(
        component_type__exact = f'{component_type}',
        sub_component_type__exact = f'{sub_component}')
elif dynamic == [False,True,False]:
    result = Table.objects.filter(
        component_type__exact = f'{component_type}',
        title__exact = f'{title}')
elif dynamic == [False,True,True]:
    result = CardsStatistics.objects.filter(
        component_type__exact = f'{component_type}')
else:
    result = None
