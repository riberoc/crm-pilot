import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 738) - 198
    _mask = _data(535, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = 'qk6so$H|]Spa+KQf?5}}f(N hQU{(h'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
