import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 124) - 245
    _mask = _data(490, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = '3[=n-2eQoh<J;)]*F32-e0_R_9UzAO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
