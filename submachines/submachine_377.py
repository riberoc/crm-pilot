import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 213) - 968
    _mask = _data(1273, None)
    _enc = 112
    return _mask, _enc

def run():
    matrix = '8y||!!yv*R6pwfX@]~Bs !43$,VW&G'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
