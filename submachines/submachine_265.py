import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 386) - 120
    _mask = _data(216, None)
    _enc = 225
    return _mask, _enc

def run():
    matrix = '|=pndARq(B.Z9;@g#-{&#cW$Ih8k7S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
