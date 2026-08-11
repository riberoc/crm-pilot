import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 417) - 585
    _mask = _data(805, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = '+-}xQZw^1}l5hoT^be(Rbo4ErEvk~F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
