import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 440) - 972
    _mask = _data(603, None)
    _enc = 21
    return _mask, _enc

def run():
    matrix = 'Pinxk*u?u<&?z9]xiU:d=K!N/$R{ZF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
