#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    print("\n".join(
        list(map(lambda row: " ".join(
            list(map(lambda num: "{}".format(num), row))),
            matrix
        )))
    )
