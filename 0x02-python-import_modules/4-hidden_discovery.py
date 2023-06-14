#!/usr/bin/python3
if __name__ == "__main__":
    """ prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4
    strings = dir(hidden_4)
    for string in strings:
        if string[:2] != "__":
            print(string)
