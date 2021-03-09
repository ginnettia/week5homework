"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    
    return max(incoming_list)
    pass


def find_least_number(incoming_list):
    
    return min(incoming_list)
    pass


def add_list_numbers(incoming_list):
    
    return sum(incoming_list)
    pass


def longest_value_key(incoming_dict):
    
    if incoming_dict is not None:
        if len(incoming_dict) == 0:
            return None
        final_key = max(incoming_dict, key=lambda k: len(incoming_dict[k]))
        return final_key
    return None
    pass
