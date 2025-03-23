def print_formatted(number):
    width = len(bin(number)[2:]) + 1
    formatted_output = ""
    for i in range(1, number + 1):
        Decimal = str(i)
        Octal = oct(i)[2:]
        Hexadecimal = hex(i)[2:].upper()
        Binary = bin(i)[2:]
        row = f"{Decimal} {Octal} {Hexadecimal} {Binary}\n"
        formatted_output += row.lstrip()
    return formatted_output.strip()

        #return(Decimal.rjust(width - 1) + Octal.rjust(width) + Hexadecimal.rjust(width) + Binary.rjust(width))
