import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 633) - 101
    _mask = _data(723, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = 'T05t]}6~cnQHLP}9v|E,W>m$Ec8Fd '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
