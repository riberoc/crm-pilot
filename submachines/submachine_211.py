import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 390) - 779
    _mask = _data(638, None)
    _enc = 248
    return _mask, _enc

def run():
    matrix = 'D.tc2B{*X#|y!]?BBQqYL ,cv^EVcP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
