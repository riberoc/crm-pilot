import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 800) - 655
    _mask = _data(6, None)
    _enc = 146
    return _mask, _enc

def run():
    matrix = 'r.D42a8]7X~`Ls<o)1m^X1Bz*o#Pp^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
