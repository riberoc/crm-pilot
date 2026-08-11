import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 701) - 592
    _mask = _data(58, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = 'tzAP]#{<|eM%9^]k:G$8ZCa+3$Yr88'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
