
def get_unique_key(str_list):
    non_unique = set()
    ret = []
    for i in str_list:
        for j in i:
            if j not in non_unique:
                ret.append([j, i])
                non_unique.add(j)
                break
    return ret

def mark_unique_key(key, string):
    return string.replace(key, '({})'.format(key), 1)

def produce_select_options(mapped_actions):
    return [[k, mark_unique_key(k, s), mapped_actions[s]]
            for k, s
            in get_unique_key(mapped_actions.keys())]
