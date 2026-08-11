import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 505) - 899
    _mask = _data(1491, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = 'o6BKJ 4raQi7,7=)pPOH:TfZhMWo`D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
