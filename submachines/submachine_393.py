import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 492) - 390
    _mask = _data(940, None)
    _enc = 173
    return _mask, _enc

def run():
    matrix = '_(xmPm7wG5H.laC9.jbXQg5 fU<Ap3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
