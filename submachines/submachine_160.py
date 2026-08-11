import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 388) - 689
    _mask = _data(658, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = 'h Pdo&CABVXSrPylL1=m)y~lor6W;!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
