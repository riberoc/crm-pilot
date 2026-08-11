import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 730) - 577
    _mask = _data(6, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = 'jYpEs5mH02QT^GNi]gS>|Cky;(dI7X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
