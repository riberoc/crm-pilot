import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 265) - 250
    _mask = _data(252, None)
    _enc = 234
    return _mask, _enc

def run():
    matrix = '|9YW<FK9+8eCl_<V$ dASxc]<V]y&+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
