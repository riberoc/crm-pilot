import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 102) - 980
    _mask = _data(897, None)
    _enc = 7
    return _mask, _enc

def run():
    matrix = '^/dxh2&Vr$!W]{8q}Yd- EQEIMl8Mz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
