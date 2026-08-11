import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 983) - 268
    _mask = _data(644, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'VxM @v-.J?CGB9Fje5bF4$dFu]GN,t'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
