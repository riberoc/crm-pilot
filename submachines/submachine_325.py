import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 746) - 831
    _mask = _data(308, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'ji<fy>lnMJgb!.4<27g?pMqTgA~_ M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
