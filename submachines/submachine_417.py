import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 646) - 687
    _mask = _data(414, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = '8GXF-)R>:zTTz%.<[f8Rjbnh6& T#b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
