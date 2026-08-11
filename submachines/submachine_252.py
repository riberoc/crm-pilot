import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 390) - 291
    _mask = _data(927, None)
    _enc = 240
    return _mask, _enc

def run():
    matrix = '0&-Rz@ ?=#4g|iwX8_]y9hootTE+]/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
