import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 748) - 826
    _mask = _data(383, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = 'k$Z44DQ(3Ylm7Vu]jDkoJw8p`sKqlm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
