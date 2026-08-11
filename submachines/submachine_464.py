import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 572) - 754
    _mask = _data(433, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '^sTJ)s7<dBI:6oc1Lf1&XZ){QsOB y'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
