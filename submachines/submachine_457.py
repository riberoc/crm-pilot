import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 520) - 409
    _mask = _data(929, None)
    _enc = 2
    return _mask, _enc

def run():
    matrix = 'am6vLiT7OT/LF|~=$L FR@t5eAcb~5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
