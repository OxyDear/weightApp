from datetime import datetime


time = str(datetime.now())


def get_part_of_day():

    hours = int(time.split()[1].split('.')[0].split(':')[0])

    if 4 <= hours < 12:
        return 'morning'
    elif 12 <= hours < 18:
        return 'afternoon'
    elif hours >= 18 or hours < 4:
        return 'evening'
