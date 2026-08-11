import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 298) - 240
    _mask = _data(235, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 'a<AZIsm%{#*I7cwB<Ftk?b!w 8_JJ>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
