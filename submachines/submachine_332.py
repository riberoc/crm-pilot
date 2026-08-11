import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 369) - 485
    _mask = _data(866, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = 'b j:t<HU&&|~&OWe;-(nG0iiZadyt8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
