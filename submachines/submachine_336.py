import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 466) - 297
    _mask = _data(138, None)
    _enc = 56
    return _mask, _enc

def run():
    matrix = '/i*7rihkyQ5v<}WldCaZX{9 KSI1e0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
