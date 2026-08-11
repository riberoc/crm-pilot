import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 204) - 611
    _mask = _data(695, None)
    _enc = 10
    return _mask, _enc

def run():
    matrix = '$65u/N}qLs{=[QZk:Cr~t#I<mU_Uet'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
