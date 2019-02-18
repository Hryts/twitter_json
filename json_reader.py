import json
import re


def get_names(data):
    res = []
    for i in data:
        res.append(i['name'])
    return res


def is_iterable(data):
    try:
        for i in data:
            pass
        return 1
    except:
        return 0


def get_dict_by_name(data, name):
    for i in data:
        if i['name'] == name:
            return i
    else:
        return -1


def count_dicts(data):
    res = 0
    for i in data:
        if type(i) == dict:
            res += 1
    return res


def view_data(data):
    """
    Lets user to view the dictionary given
    """
    try:

        data_type = re.findall('\'(.* ?)\'', str(type(data)))[0]
        print('Current type: {}'.format(data_type))
        print()
        if type(data) == dict:
            for key in data:
                print(key)
            next_key = input('Enter next key to view: ')
            view_data(data[next_key])
        elif count_dicts(data) > 0 and data:
            print('There are {} dicts in here'.format(count_dicts(data)))
            print('Names in dicts:')
            for name in get_names(data):
                print(name)
            next_name = input('Next name: ')
            view_data(get_dict_by_name(data, next_name))
        elif count_dicts(data) == 0:
            print('No dicts here')
            show_all = input('Would you like to see all this value [y/n] ')
            if show_all == 'y':
                print(data)
    except:
        print('Something has gone wrong')


if __name__ == '__main__':
    with open('user_friends.json') as f:
        data = json.load(f)
    view_data(data)