import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 146) - 672
    _mask = _data(974, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = 'E<c3@1M5g2;kJ:n=G-QPilvV+m6r^O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
