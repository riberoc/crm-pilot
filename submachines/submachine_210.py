import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 666) - 299
    _mask = _data(832, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = 'w+u.<k@bZe7!o@wN=Y|h7`Jf0hcCrk'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
