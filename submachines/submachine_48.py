import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 616) - 158
    _mask = _data(682, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = '8]RlERT&n|v@w9x+t96S@H51__ZQZ0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
