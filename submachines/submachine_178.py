import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 331) - 293
    _mask = _data(51, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'filh21&4@B9_4Aw_ZsRVCY(XDVv-h,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
