import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 172) - 797
    _mask = _data(838, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = 'cwF(:6G|[4.2Inyty9,{RLMJ9Kqy4 '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
