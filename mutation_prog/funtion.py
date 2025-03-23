def mutation(string,position,letters):
    if position < 0 or position >= len(string):
        return "Invalid position"
    new_string = string[:position] + letters + string[position + 1:]
    return new_string
