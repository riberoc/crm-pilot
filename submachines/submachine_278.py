import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 259) - 979
    _mask = _data(1396, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = 'C2* enHQ<eX}zNJtVgX2T?IfQGamnu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
