import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 518) - 344
    _mask = _data(896, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '{azdVaN=Mpjyr|4(tx-hz@x_/.S%k%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
