import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 285) - 838
    _mask = _data(1319, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = '5j;HeH:9O*azB p7SgkS}z$/zPinh@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
