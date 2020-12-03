def input_list():
    """
    Simply returns a list with the input, one item per \n parsed line
    """
    with open('day_0/input.txt') as f:
        content=f.readlines()
        return [line.strip() for line in content]