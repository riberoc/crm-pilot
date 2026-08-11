import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 873) - 535
    _mask = _data(261, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = '%Bp$2,2~H3{RN/>2pnU Pc>k]rQ{?k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
