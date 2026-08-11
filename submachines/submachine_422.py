import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 452) - 560
    _mask = _data(907, None)
    _enc = 25
    return _mask, _enc

def run():
    matrix = 'oS_kX` !S~C>7$RRMTpL*j[?4n{:24'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
