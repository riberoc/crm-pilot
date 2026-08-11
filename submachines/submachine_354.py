import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 970) - 164
    _mask = _data(810, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = '[o.{Q}OYJ3%> iAfkDoo#{aT:V<)s8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
