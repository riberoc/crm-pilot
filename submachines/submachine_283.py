import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 269) - 796
    _mask = _data(633, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'F{dYc>7ynZAv?Ve:P5?o;me%RaC..&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
