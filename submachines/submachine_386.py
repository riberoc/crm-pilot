import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 529) - 358
    _mask = _data(898, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = 'st<mc9e)h2K@?N97F%s%;M@f >qU?-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
