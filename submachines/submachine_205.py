import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 823) - 506
    _mask = _data(433, None)
    _enc = 155
    return _mask, _enc

def run():
    matrix = 'LYQf8ZkEFrE5XQrTPwY~(R6 WEjCu7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
