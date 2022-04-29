def print_formatted(number):
    # your code goes here

    print('\n'.join([x for x in
                     [f"{str(i).rjust(len(bin(number)[2:]))} {oct(i)[2:].rjust(len(bin(number)[2:]))} "
                      f"{hex(i).upper()[2:].rjust(len(bin(number)[2:]))} {bin(i)[2:].rjust(len(bin(number)[2:]))}"
                      for i in range(1, number + 1)]]))


n = int(input())
print_formatted(n)
