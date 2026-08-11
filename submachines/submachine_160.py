import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 207) - 737
    _mask = _data(910, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'PgK>c?uIDJaSs?Y7jX}JCjFwq<567,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
