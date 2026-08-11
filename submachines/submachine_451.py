import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 782) - 318
    _mask = _data(593, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = '^23oH4qE:qgE_eVGkN!Et[H`HX1Kg,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
