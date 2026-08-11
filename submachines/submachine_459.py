import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 832) - 620
    _mask = _data(463, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = 'g66`IC58P`lS+24^]+Z _q[A-41aKz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
