import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 297) - 714
    _mask = _data(574, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = 'uWiGbf)C3M00,cWWm~AhKc%vAA/8>9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
