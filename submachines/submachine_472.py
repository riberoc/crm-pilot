import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 637) - 767
    _mask = _data(260, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'GF/J|_%XTbYvAKa N(XGuZbExP>$Cm'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
