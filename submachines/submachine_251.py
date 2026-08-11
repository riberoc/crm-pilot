import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 915) - 501
    _mask = _data(497, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'FjzE[jW7R~]{5< pCm<p5H.~~l[}!w'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
