import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 529) - 800
    _mask = _data(352, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '<Tq_~}zyn37-* H8}A5qdxdB~`.x_-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
