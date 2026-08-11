import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 478) - 445
    _mask = _data(990, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'bD/64objz8c&S8yttG7YK >9k]IPFv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
