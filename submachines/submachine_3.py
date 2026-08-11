import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 898) - 535
    _mask = _data(335, None)
    _enc = 185
    return _mask, _enc

def run():
    matrix = 'FZLxre{ld&:7[oj [^{!+BQ6YaRbW+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
