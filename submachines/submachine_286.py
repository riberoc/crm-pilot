import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 445) - 867
    _mask = _data(514, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = '<gcpikjSKtO9B;nXMT~q;>in97Y*jl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
