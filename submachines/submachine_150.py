import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 264) - 765
    _mask = _data(672, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = 'fZH-4`#c(ADH9e+`G+!JnhAE;.^Fnx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
