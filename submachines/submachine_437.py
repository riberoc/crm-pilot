import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 938) - 566
    _mask = _data(322, None)
    _enc = 161
    return _mask, _enc

def run():
    matrix = 'r?`Tsl#pR-wC99*|.0Y vwIU6hML5i'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
