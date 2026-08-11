import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 404) - 147
    _mask = _data(208, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = ' ~k0EGR@SaL5w>-L;LtFT@bK),o08^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
