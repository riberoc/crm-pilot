import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 405) - 366
    _mask = _data(42, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = 'a11[/%e(~sfTyv{[H;Yfoh5?fEv{%x'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
