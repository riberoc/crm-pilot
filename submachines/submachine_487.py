import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 722) - 486
    _mask = _data(246, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = '+Ser%$&h+p ,cF+|X2<EkHvpAj}IjO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
