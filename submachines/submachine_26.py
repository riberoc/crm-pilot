import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 128) - 692
    _mask = _data(592, None)
    _enc = 18
    return _mask, _enc

def run():
    matrix = ')H3{5o_f!T|qPl >dAo6b0O!%8s}f~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
