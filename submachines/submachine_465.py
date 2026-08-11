import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 493) - 116
    _mask = _data(140, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = 'gFJh ppLSxLpkvzH1Gjrjosz4?]V(e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
