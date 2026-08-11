import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 368) - 842
    _mask = _data(1363, None)
    _enc = 206
    return _mask, _enc

def run():
    matrix = 'kkKgV+BJrKo__rmOo1O0!R: 8kz?w8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
