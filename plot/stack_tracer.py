from pylab import plot, show


level = 0
trail = [level]

def tracer(func):
    def wrapper(*args, **kw):
        if 'tail' in kw:
            tail = kw.pop('tail')
        else:
            tail = False

        global level, trail
        if not tail:
            level += 1
            trail.append(level)
        ret = func(*args, **kw)
        if not tail:
            level -= 1
            trail.append(level)
        return ret
    return wrapper


def draw():
    plot(trail)
    show()


def move(from_, to):
    print from_, '->', to

@tracer
def hanoi(n, from_, to, assist):
    if n <= 0:
        return

    hanoi(n-1, from_, assist, to)
    #move(from_, to)
    hanoi(n-1, assist, to, from_, tail=True)


@tracer
def fib(n):
    '''fibonacci'''
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)


def draw1():
    hanoi(3, 'F', 'T', 'A')
    draw()


def draw2():
    fib(5)
    draw()

draw2()
