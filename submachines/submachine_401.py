import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 463) - 520
    _mask = _data(784, None)
    _enc = 206
    return _mask, _enc

def run():
    matrix = '4_kzdtQ&}LEfiKEGI$$Gv#G|d 7DBO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
