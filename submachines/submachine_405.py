import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 205) - 691
    _mask = _data(949, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = '}_LXOI#]6aU-.w{)M#:o)DMSM/S02a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
