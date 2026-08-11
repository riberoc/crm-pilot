import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 761) - 440
    _mask = _data(154, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = ']i|V,17D7C>^8`H%/91?p8ihMWKqvs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
