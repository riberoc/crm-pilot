import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 829) - 199
    _mask = _data(618, None)
    _enc = 155
    return _mask, _enc

def run():
    matrix = '#OAcrdj}&H` w9c8S<(hj?g&ByQvl:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
