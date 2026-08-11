import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 579) - 685
    _mask = _data(491, None)
    _enc = 239
    return _mask, _enc

def run():
    matrix = 'y9UqLo/-YGNWlrMqcZ+ln%9aK#.<n3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
