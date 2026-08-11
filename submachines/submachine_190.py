import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 814) - 696
    _mask = _data(155, None)
    _enc = 225
    return _mask, _enc

def run():
    matrix = 'C2l1ssGa7<p1ruS7pq,(6SmEJ(gH X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
