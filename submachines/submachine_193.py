import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 178) - 840
    _mask = _data(795, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = 'd629W 1ZizrZ`!y=7Gz<tX>_Y`>_k;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
