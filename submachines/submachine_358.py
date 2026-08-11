import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 611) - 718
    _mask = _data(381, None)
    _enc = 84
    return _mask, _enc

def run():
    matrix = 'aL|Df0LI[vkfd@j6Dp1q%n|=*%^tLZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
