# sum of multiples of 3 and 5 below 1000

def get_multiples(N):
    multiples = set()

    for x in range(0, N):
        if x % 3 == 0:
            multiples.add(x)
        if x % 5 == 0:
            multiples.add(x)

    return multiples

if __name__ == '__main__':
    max_num = 1000
    multiples = get_multiples(max_num)
    print(multiples)
    print(f"Sum of multiples of 3 or 5 below {max_num} is {sum(multiples)}")
