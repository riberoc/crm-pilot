import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 575) - 561
    _mask = _data(120, None)
    _enc = 26
    return _mask, _enc

def run():
    matrix = 'r<=G+2&M-v_PtS@tt6^%ufD%rmlyc)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
