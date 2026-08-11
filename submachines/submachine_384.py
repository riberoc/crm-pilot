import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 535) - 842
    _mask = _data(455, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = '7u%weOM@:4z]*?v3[.-Cal_ g?ULVb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
