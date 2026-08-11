import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 954) - 284
    _mask = _data(633, None)
    _enc = 173
    return _mask, _enc

def run():
    matrix = 'E.N7@(?Hdp w6h7q4VOPz8)5V2r*P^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
