import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 903) - 495
    _mask = _data(446, None)
    _enc = 82
    return _mask, _enc

def run():
    matrix = 'O8lP:vm^{J{J-krpl>~TQ[*ekeQ3])'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
