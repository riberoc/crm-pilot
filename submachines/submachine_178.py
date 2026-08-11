import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 197) - 412
    _mask = _data(739, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = '+<pT[g 5-1+;ODu?l>;!+^_-#<FN8l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
