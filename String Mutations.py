def mutate_string(string, position, character):
    #string = raw_input()
     # insert the new string between "slices" of the original
    return string[:position] + character + string[position + 1:]
