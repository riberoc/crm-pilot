import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 778) - 134
    _mask = _data(597, None)
    _enc = 194
    return _mask, _enc

def run():
    matrix = 'LpFzF1)VxkM|QKph)w3Nz8<8FMS 5_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
