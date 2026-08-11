import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 203) - 305
    _mask = _data(426, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = 'N +4*tJ)8d|`~VnOYbaryI!=Ub[`9('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
