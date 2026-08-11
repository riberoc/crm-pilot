import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 629) - 252
    _mask = _data(953, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = '@Bao6q<sO#3t39;14Eicy!K@h(J Hc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
