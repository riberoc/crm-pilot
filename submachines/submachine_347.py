import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 690) - 887
    _mask = _data(1785, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'EoM;HBF r2:8C?]TTu_lHZF+Q]eL-n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
