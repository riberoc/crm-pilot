import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 441) - 671
    _mask = _data(685, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = 'f>]<BLc7?ntd274lg/w8st}{>kOF.l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
