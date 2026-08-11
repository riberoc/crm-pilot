import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 520) - 777
    _mask = _data(355, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'ca5Gxz<SGOv0t4(0Rz0&(Ug(lSxNIO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
