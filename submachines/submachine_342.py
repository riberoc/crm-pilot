import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 219) - 328
    _mask = _data(744, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = '7Kjx8}Gse:NJC9xvrP 9kN?cBHr7oA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
