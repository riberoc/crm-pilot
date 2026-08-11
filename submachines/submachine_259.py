import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 802) - 110
    _mask = _data(1004, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = '>`o+6zt-ue6QHI`$:%|YOs,V: Ekw+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
