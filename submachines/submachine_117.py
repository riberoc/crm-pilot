import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 691) - 383
    _mask = _data(154, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = '6@0Yc};]@w#xLaI:!H0 0,#q-qZ=Z,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
