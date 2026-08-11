import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 729) - 833
    _mask = _data(446, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = '@@aN[_-!GDN_nTz7Y=E{}ech=kP`<!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
