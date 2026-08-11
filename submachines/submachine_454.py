import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 224
    _mask = _data(467, None)
    _enc = 111
    return _mask, _enc

def run():
    matrix = 'h_H?|m~tQiTy=OM(-G3F1EQ% +QKZ}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
