import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 770) - 466
    _mask = _data(296, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = ' br+qz&ts_N!=j1NoP1!@-^bt2]GZV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
