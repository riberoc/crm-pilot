import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 764) - 376
    _mask = _data(179, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'OfVJW9.7lgL[Q/]u_q)<X_^d^$QHWg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
