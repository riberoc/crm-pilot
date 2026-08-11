import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 824) - 603
    _mask = _data(417, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = 't0 8yh(rGV6YG~}McYHg0?J6q$]}8U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
