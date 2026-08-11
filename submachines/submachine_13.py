import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 385) - 785
    _mask = _data(601, None)
    _enc = 211
    return _mask, _enc

def run():
    matrix = 'bucm|-bt(DSkKiqCGn*i ~p!mQ]@FR'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
