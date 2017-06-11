def get_average(num_list):
    if len(num_list) != 0:
        return sum(num_list) / len(num_list)
    else:
        return 0


def get_variance(num_list):
    if len(num_list) != 0:
        return sum([(sum(num_list) / len(num_list) - num)**2 for num in num_list]) / len(num_list)
    else:
        return 0


def remove_overlap(word_list):
    return list(set(word_list))


def round_over_5(num_list):
    return [round(num) for num in num_list if num >= 5]
