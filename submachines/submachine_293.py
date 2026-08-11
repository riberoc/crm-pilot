import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 953) - 286
    _mask = _data(728, None)
    _enc = 85
    return _mask, _enc

def run():
    matrix = 'dOEw^e2)()GLA~r8(-pjkre^bS3{`s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
