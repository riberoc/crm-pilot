import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 339) - 423
    _mask = _data(169, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = '`Hl%DXv._BN i:x-Oo/tah>^b6{p3L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
