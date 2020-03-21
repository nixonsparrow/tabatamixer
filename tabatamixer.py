import json
import time
import random


def open_exercises_json():
    with open('exercises.json', 'r') as read_file:
        exercises = json.load(read_file)
        return exercises


def write_exercises_json(x):
    with open('exercises.json', 'w') as write_file:
        json.dump(x, write_file)


def open_json(name):
    with open(name + '.json', 'r') as read_file:
        content = json.load(read_file)
        return content


def write_json(name, content):
    with open(name + '.json', 'w') as write_file:
        json.dump(content, write_file)


def create_tabata_set(number_of_exercises=4, chosen_level=3):
    exercises_database = open_exercises_json()

    # get list of proper difficulty level exercises
    difficulty_set = False
    if number_of_exercises == 2:
        if chosen_level == 1:
            difficulty_set = [1, 2]
        if chosen_level == 2:
            difficulty_set = [2, 2]
        if chosen_level == 3:
            difficulty_set = [2, 3]
    elif number_of_exercises == 4:
        if chosen_level == 1:
            difficulty_set = [1, 1, 2, 2]
        if chosen_level == 2:
            difficulty_set = [1, 2, 2, 3]
        if chosen_level == 3:
            difficulty_set = [2, 2, 3, 3]
    else:
        print('Wrong exercises setting, passing default set.')
        difficulty_set = [1, 2, 2, 3]

    current_target = None      # legs / core / pull / push
    current_purpose = None     # cardio / strength

    # create list of ids from you choose
    list_of_available_ids = []
    for e in exercises_database:
        list_of_available_ids.append(e['id'])

    # here will go chosen exercises
    tabata_final_set = []

    try:
        # main choosing loop
        while difficulty_set:
            # pick random number from remaining then delete it from the list
            chosen_exercise_id = random.choice(list_of_available_ids)

            chosen_exercise = next(item for item in exercises_database if item['id'] == chosen_exercise_id)

            if current_target != chosen_exercise['target'] and current_purpose != chosen_exercise['purpose'] \
                    and difficulty_set[0] == chosen_exercise['difficulty']:
                tabata_final_set.append(chosen_exercise)
                list_of_available_ids.remove(chosen_exercise_id)
                del difficulty_set[0]
                current_purpose = chosen_exercise['purpose']
                current_target = chosen_exercise['target']

    except IndexError:
        print('There is no possible way to make such tabata set.')

    for ex in tabata_final_set:
        print(ex['name'])

    return tabata_final_set


def tabata_music():
    tabata_list = open_json('tabatamusic')
    return random.choice(tabata_list)


def add_new_tabata_music():
    pass


if __name__ == '__main__':
    add_new_tabata_music
    pass
