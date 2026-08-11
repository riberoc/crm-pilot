import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 361) - 391
    _mask = _data(140, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = 'RuTCZK7M-a>tBwXGn~YnIh(8woSnX.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
