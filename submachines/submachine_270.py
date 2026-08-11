import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 516) - 509
    _mask = _data(172, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'O woPb#@w`2b9:n1NX)gX4O55hYyKY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
