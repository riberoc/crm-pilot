import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 676) - 348
    _mask = _data(773, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = 'P<;&51gtdt..u JAL:R8lC#Ke{[JW='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
