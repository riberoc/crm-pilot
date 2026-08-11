import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 110) - 277
    _mask = _data(494, None)
    _enc = 115
    return _mask, _enc

def run():
    matrix = 'IAQ+`sTm{mE(}rhZZSF#?=w* JtjIp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
