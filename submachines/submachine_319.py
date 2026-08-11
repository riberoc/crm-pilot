import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 802) - 702
    _mask = _data(474, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = ']8&GUmAl4o1Em0:FXW0EO_Aq!iV&DW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
