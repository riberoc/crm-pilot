import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 284) - 362
    _mask = _data(157, None)
    _enc = 6
    return _mask, _enc

def run():
    matrix = 'i:(:d#u<YVV+t]~1{ !j7tUl@u-JTl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
