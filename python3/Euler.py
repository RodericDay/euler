from math import sqrt, ceil, floor
import itertools
import functools
import operator
import collections
from fractions import Fraction

def subsequences(iterable, length):
    '''
    >>> [''.join(seq) for seq in subsequences("Hello world!", 10)]
    ['Hello worl', 'ello world', 'llo world!']
    '''
    yield from zip(*[iterable[start:] for start in range(length)])

def product(iterable):
    '''
    >>> product([3, 3, 5])
    45
    '''
    return functools.reduce(operator.mul, iterable)

def prime_sieve(n):
    '''
    >>> g = prime_sieve(100)
    >>> [next(g) for _ in range(5)]
    [2, 3, 5, 7, 11]
    '''
    sieve = [True] * int(n+1) # this is not identical to a list comprehension!
    sieve[0] = sieve[1] = False
    for p in (p for p, is_prime in enumerate(sieve) if is_prime):
        if p**2 < n: sieve[2*p::p] = [False] * int(n/p-1)
        yield p

def convergents(chain):
    '''
    >>> g = convergents([1, 2])
    >>> [next(g) for _ in range(4)][1:]
    [Fraction(3, 2), Fraction(7, 5), Fraction(17, 12)]
    '''
    first, *rest = chain
    repeating = itertools.cycle(rest)
    f = Fraction(first)
    m = next(repeating)
    fn = Fraction(1 + f*m, m)
    for m in repeating:
        yield f
        n = f.numerator   + m * fn.numerator
        d = f.denominator + m * fn.denominator
        f, fn = fn, Fraction(n, d)

def cfrac(S):
    '''
    >>> cfrac(7)
    [2, 1, 1, 1, 4]
    '''
    alist = []
    seen = set()
    m = m0 = 0
    d = d0 = 1
    a = a0 = floor(sqrt(S))
    if a0**2 == S: return [a0]
    while (m, d, a) not in seen:
        seen.update({(m, d, a)})
        alist.append(a)
        m = d*a - m
        d = ( S - m**2 ) // d
        a = ( a0 + m ) // d
    return alist


if __name__ == '__main__':
    import doctest
    doctest.testmod()
