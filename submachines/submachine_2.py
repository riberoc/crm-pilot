import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 671) - 909
    _mask = _data(321, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = '*IjYAX?afeTyQP02n0j0Z`2lT$jQ9.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
