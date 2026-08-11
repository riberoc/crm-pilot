import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 278) - 159
    _mask = _data(26, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = 'Z_4vB5_[*7 Gk18G@?3rRf);3{s*f='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
