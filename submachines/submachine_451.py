import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 748) - 704
    _mask = _data(57, None)
    _enc = 15
    return _mask, _enc

def run():
    matrix = 'hps3))jkqZD7t_[v1tM`#wGA<W bQ6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
