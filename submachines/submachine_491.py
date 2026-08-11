import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 771) - 872
    _mask = _data(184, None)
    _enc = 67
    return _mask, _enc

def run():
    matrix = 'weh%ssHE4BHfw$?G qVtoQeqDyp+7|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
