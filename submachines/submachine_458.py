import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 744) - 981
    _mask = _data(1725, None)
    _enc = 128
    return _mask, _enc

def run():
    matrix = 'ns12:m7sfNVTbq0-EOwsVY:qIg?T/,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
