import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 426) - 131
    _mask = _data(367, None)
    _enc = 90
    return _mask, _enc

def run():
    matrix = 'P(sx?n;&HE]05x_k4I7ik~a|t>)[;1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
