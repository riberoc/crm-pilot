import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 609) - 938
    _mask = _data(446, None)
    _enc = 61
    return _mask, _enc

def run():
    matrix = '2(t@(Z3j A0sdGXkmtZ:q<i6[e4AeT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
