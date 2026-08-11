import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 549) - 963
    _mask = _data(1643, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = '~WCIQ)K B%3iK>nf__:GS5FzJAb@!d'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
