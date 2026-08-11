import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 277) - 665
    _mask = _data(1007, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = 'Dk`#1i _6FYk;;H@]d3ucb}x?%P,+o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
