def multiply_dict(name_list, multi):
    return {key: value * multi for key, value in name_list.items()}


def merge_dict(dict1, dict2):
    for name in dict2.items():
        if name in dict2:
            dict1[name] += dict2[name]
        else:
            dict1.update(name, dict2[name])
    return dict1


def sort_dict_by_value(name_dict):
    rev_dict = {value: key for key, value in name_dict.items()}
    return [rev_dict[num] for num in list(rev_dict).sort(reverse=True)]
