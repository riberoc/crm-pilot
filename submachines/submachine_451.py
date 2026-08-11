import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 357) - 984
    _mask = _data(1400, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = '<Aa1+~8!_#6%n7v/q9.q>pTTa?XSUP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
