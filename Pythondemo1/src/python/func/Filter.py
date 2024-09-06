def main():
    for n in primes():
        if n < 100:
            print(n)
        else:
            break


def _odd_iter():
    n = 2
    while True:
        n = n + 1
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


main()