import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 217) - 494
    _mask = _data(579, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = '^-Vn}=50%K] 8W2<mlkIN,+lVE^ovP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
