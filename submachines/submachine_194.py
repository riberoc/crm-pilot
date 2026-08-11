import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 400) - 388
    _mask = _data(105, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = '] PY=FNNPxG^!w5cKxMmH{XE7P`wyN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
