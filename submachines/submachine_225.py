import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 776) - 979
    _mask = _data(1934, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = 'g;X></rO-#3n46;*hyTDy|vPEhzZ ]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
