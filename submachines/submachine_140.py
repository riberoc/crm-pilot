import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 580) - 933
    _mask = _data(412, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = 'kw?c@516zsRKl`P O:)-|83gR0Xs8.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
