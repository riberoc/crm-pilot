import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 113) - 366
    _mask = _data(493, None)
    _enc = 53
    return _mask, _enc

def run():
    matrix = '9]7|c*sctxQdOkfiW4-g)1|=JsCi}.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
