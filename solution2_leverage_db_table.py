#TODO: add sample
# Table query is dependent on database.
#In this example we leverage a Django table and static dictionary to execute our functions
#Static dictionary ensures only authorized functions may be called from database to avoid compromising code injections).

database_query(part,component,sub_component):
    dynamic = [part==None, component==None, sub_component==None]
    if dynamic == [False,False,False]:
        result = Table.objects.filter(
            part__exact = f'{part}',
            component__exact = f'{component}',
            title__exact = f'{sub_component}')
    elif dynamic == [False,False,True]:
        result = Table.objects.filter(
            part__exact = f'{part}',
            component__exact = f'{component}')
    elif dynamic == [False,True,False]:
        result = Table.objects.filter(
            part__exact = f'{part}',
            sub_component__exact = f'{sub_component}')
    elif dynamic == [False,True,True]:
        result = CardsStatistics.objects.filter(
            part__exact = f'{part}')
    else:
        result = None
    return result
