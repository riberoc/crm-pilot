import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 977) - 834
    _mask = _data(39, None)
    _enc = 183
    return _mask, _enc

def run():
    matrix = 'hNu w%+]K!Pd@%mZhua[KX3=qv3=H,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
