import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 854) - 948
    _mask = _data(163, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'tUE |2Hl[!MK>AGP+.RqP!(5ZZ[g7o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
