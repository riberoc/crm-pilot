import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 246) - 457
    _mask = _data(646, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = '&*(.P%GW5gob`~mq%/y i5w!n!M6=-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
