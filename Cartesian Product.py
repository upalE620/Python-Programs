from itertools import product


def cartesian_product(arr1, arr2):
    for i in list(product(arr1, arr2)):
        print(i, end=" ")


# Driver Function
if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    cartesian_product(arr1, arr2)
