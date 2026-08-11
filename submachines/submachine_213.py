import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 115) - 285
    _mask = _data(611, None)
    _enc = 246
    return _mask, _enc

def run():
    matrix = 'aP6nO amwlTJ/:7:&w7{)*XWi.ut)='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
