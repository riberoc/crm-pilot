import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 279) - 749
    _mask = _data(619, None)
    _enc = 132
    return _mask, _enc

def run():
    matrix = '{}thfcty>=G (C])qW}}:7o3QY,LNI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
