import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 744) - 379
    _mask = _data(244, None)
    _enc = 188
    return _mask, _enc

def run():
    matrix = '<Y9P)Z&bf?albk7[Nmf@>nXz{1<MY '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
