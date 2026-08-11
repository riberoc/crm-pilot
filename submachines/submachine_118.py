import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 444) - 189
    _mask = _data(198, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = 'i9x4o {BT@tB9Tgxa]iZwue-Q3ZF:s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
