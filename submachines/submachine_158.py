import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 275) - 214
    _mask = _data(210, None)
    _enc = 252
    return _mask, _enc

def run():
    matrix = 'Z7FHO|J~QC,=4~OlysC0y*H 1IY@W&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
