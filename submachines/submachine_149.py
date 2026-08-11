import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 280) - 318
    _mask = _data(187, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = 'E6Um_E(XBo0#!5*D(fN@jhujjz)2Z.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
