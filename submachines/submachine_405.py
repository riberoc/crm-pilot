import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 512) - 972
    _mask = _data(1700, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = '#kvaztDbN4e2; ,s!A_l~yM=A,./;J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
