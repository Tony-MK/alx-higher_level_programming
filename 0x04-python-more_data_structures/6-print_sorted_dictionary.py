#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort(reverse=False)
    print(
            "\n".join([
                    "{}: {}".format(key, a_dictionary[key])
                    for key in sorted_keys
                ])
    )
