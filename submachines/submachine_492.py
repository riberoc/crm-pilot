import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 492) - 115
    _mask = _data(359, None)
    _enc = 13
    return _mask, _enc

def run():
    matrix = 'd^r2--#bqY7y0R~u:JLh( q/T3o53e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
