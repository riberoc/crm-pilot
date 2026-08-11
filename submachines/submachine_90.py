import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 114) - 856
    _mask = _data(1022, None)
    _enc = 54
    return _mask, _enc

def run():
    matrix = 'L|msIFRSa.3xzqyl80Pg<k^8TITxq~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
