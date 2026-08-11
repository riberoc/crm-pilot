import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 217) - 134
    _mask = _data(444, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = ';_?#A^?gR9R<]y;N231idfMfgc|35%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
