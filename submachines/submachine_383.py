import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 783) - 431
    _mask = _data(385, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'rKHQU/!r_|A@E4& EfoXDJ8L$<eP>D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
