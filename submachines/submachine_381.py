import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 511) - 975
    _mask = _data(1408, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = 'zSsheF 4y[g-d[^4omg;0xGVoLZnc)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
