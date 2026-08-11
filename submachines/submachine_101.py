import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 169) - 835
    _mask = _data(966, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = 'g)Zq]0W1|pA~?P$kS<bwrI3DVvGGt_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
