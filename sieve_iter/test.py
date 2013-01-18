import sieve

def test1():
    s = sieve.sieve()
    i = iter(s)
    assert i.next() == 3

def test2():
    s = sieve.sieve()
    i = iter(s)
    i.next()
    assert i.next() == 5

def test3():
    s = sieve.sieve()
    i = iter(s)
    i.next()
    i.next()
    assert i.next() == 7

test1()
test2()
test3()
