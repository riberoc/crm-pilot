import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 939) - 507
    _mask = _data(507, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'z3h+U{,~54w rS|vzxwOFjeb[FE]k:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
