import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 858) - 381
    _mask = _data(298, None)
    _enc = 229
    return _mask, _enc

def run():
    matrix = '95v8v>Eh6;rbe@b.=9#hsf b5$cW~M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
