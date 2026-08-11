import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 811) - 914
    _mask = _data(1808, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'B3J8lljPb6s to:qtHO|Q13~9I)qYe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
