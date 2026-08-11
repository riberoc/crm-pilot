import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 207) - 206
    _mask = _data(335, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'nyb^ryib@@i,W E/ZACTZid~>CkAC`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
