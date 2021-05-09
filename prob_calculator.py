import copy
import random


class Hat:

    def __init__(self, **kwargs):

        balls = []
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(
                    f'Ball value expected to be int, but received {type(value)}: {repr(value)}.')

            for _ in range(value):
                balls.append(f'{key}')

        if len(balls) < 1:
            raise ValueError(
                f'The Hat object should contain at least one ball.')
        self.contents = balls

    def draw(self, num_balls) -> list:

        removed_balls = []
        for _ in range(num_balls):
            end_range = len(self.contents) - 1
            if self.contents:
                idx = random.randint(0, end_range)
                item = self.contents.pop(idx)
                removed_balls.append(item)
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    match_count = 0
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        obtained_balls_list = temp_hat.draw(num_balls_drawn)
        obtained_balls_dict = list_to_dict(obtained_balls_list)

        if is_subset(expected_balls, obtained_balls_dict):
            match_count += 1

    return match_count / num_experiments


def list_to_dict(lst):
    '''
    Convert a `list` into a `dict` where list item is the key and counter number is the value.
    '''
    dct = {}
    for item in lst:
        dct[item] = dct.get(item, 0) + 1

    return dct


def is_subset(dct1_expected, dct2_obtained):
    '''
    Check if items in `dct1_expected` has at least equal number 
    of items in `dct2_obtained` returns `True` otherwise `False`.
    '''
    subset = True
    for key, value in dct1_expected.items():
        if value > dct2_obtained.get(key, 0):
            subset = False
    return subset
