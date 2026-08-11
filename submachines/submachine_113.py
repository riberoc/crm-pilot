import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 324) - 660
    _mask = _data(1007, None)
    _enc = 31
    return _mask, _enc

def run():
    matrix = '8|rz.O2(oMFl)<:k+cgueXCNDjZEb<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
