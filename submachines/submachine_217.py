import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 560) - 900
    _mask = _data(1549, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = 'RJ5oRrQ10 I;c#MhaF.E2wshQ0NrSE'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
