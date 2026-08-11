import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 727
    _mask = _data(533, None)
    _enc = 174
    return _mask, _enc

def run():
    matrix = ')O=9-Ps(i4eXA&T%8iuulJ-%nMU(gX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
