import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 109) - 893
    _mask = _data(1097, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = '+FmD{hS~w3d|HEtQUa# @r[U-zCPJS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
