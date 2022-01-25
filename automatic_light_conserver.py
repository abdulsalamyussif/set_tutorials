class lectureHall:
    def __init__(self,name, is_empty, light_on):
        self.name = name
        self.is_empty = is_empty
        self.light_on = light_on

class Office:
    def __init__(self, name, is_empty, light_on):
        self.name = name
        self.is_empty = is_empty
        self.light_on = light_on

lecture_hall = [
    lectureHall('Lecture hall 1', False, True),
    lectureHall('Lecture hall 2', True, True),
    lectureHall('Lecture hall 3', False, False),
    lectureHall('Lecture hall 4', False, True),
    lectureHall('Lecture hall 5', True, True),
    lectureHall('Lecture hall 6', False, True),
    lectureHall('Lecture hall 7', True, False),
    lectureHall('Lecture hall 8', False, False),
    lectureHall('Lecture hall 9', True, True),
    lectureHall('Lecture hall 10', False, True),
    lectureHall('Lecture hall 11', True, True),
    lectureHall('Lecture hall 11', False, True)

]

office = [
    Office('Office 1', False, True),
    Office('Office 2', True, False),
    Office('Office 3', False, False),
    Office('Office 4', True, False),
    Office('Office 5', True, True),
    Office('Office 6', False, False),
    Office('Office 7', True, True),
    Office('Office 8', True, False),
    Office('Office 9', False, False),
    Office('Office 10', False, True),
    Office('Office 11', False, False),
    Office('Office 12', True, True),
]
    

def conserve_energy(list_of_objs):
    count = 0
    for room in list_of_objs:
        if room.is_empty and room.light_on:
            count = count + 1
            print(f'{room.name} lights turned off!')
    return count


def inspect_halls():
    print('Inspecting lecture halls.....')
    totals = conserve_energy(lecture_hall)
    print(f'------> A total of {totals} lights turned off.')
    print('========================')


def inspect_offices():
    print('Inspecting offices.....')
    totals = conserve_energy(office)
    print(f'------> A total of {totals} lights turned off.')
    print('========================')

inspect_halls()
inspect_offices()


        