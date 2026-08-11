import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 963) - 822
    _mask = _data(5, None)
    _enc = 141
    return _mask, _enc

def run():
    matrix = ':c6Tz3x4d5g_J{;n|~615^XB{zL!M '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
