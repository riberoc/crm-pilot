import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 584) - 725
    _mask = _data(409, None)
    _enc = 252
    return _mask, _enc

def run():
    matrix = 'TEp<HP4[XYZFX~b*:BS|~{l~ndL4S`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
