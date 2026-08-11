import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 541) - 167
    _mask = _data(899, None)
    _enc = 244
    return _mask, _enc

def run():
    matrix = 'u0qw6FK7i%z;6xhiG,+vYfTQi6O^7x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
