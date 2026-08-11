import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 197) - 937
    _mask = _data(1208, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'HF|YJspqod4 (]K&=0EW493B!r@;k/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
