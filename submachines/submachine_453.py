import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 426) - 736
    _mask = _data(701, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '!R_Nr0-H^OEY4yNE=<i}c&L/ 2!Kd)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
