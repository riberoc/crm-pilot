import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 161) - 509
    _mask = _data(621, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = '+PO_>F1ofNlRZSHMr B4]q|.|*$(<)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
