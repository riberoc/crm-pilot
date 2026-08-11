import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 577) - 356
    _mask = _data(914, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = 'VNH%DPy-|>^)Ag`~Zi}1Dc9o&:i|oW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
