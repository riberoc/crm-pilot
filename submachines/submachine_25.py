import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 472) - 415
    _mask = _data(863, None)
    _enc = 224
    return _mask, _enc

def run():
    matrix = 'kah<~6=k }wZ`ZfM-jGA#e.qPdo+;('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
