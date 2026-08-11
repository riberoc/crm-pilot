import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 789) - 672
    _mask = _data(503, None)
    _enc = 64
    return _mask, _enc

def run():
    matrix = '|C `$tRcIGU*,Rq8f$~E,cH+`/^}^n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
