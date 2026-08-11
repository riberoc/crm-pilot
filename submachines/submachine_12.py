import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 704) - 179
    _mask = _data(929, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = '^!ZducCTOxO(c!qb{ 4]Jx|qT>2W)|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
