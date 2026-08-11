import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 484) - 216
    _mask = _data(180, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = 'U>/7O1deO>2a {oFq_VykU22k$nhkU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
