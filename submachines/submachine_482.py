import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 535) - 121
    _mask = _data(811, None)
    _enc = 218
    return _mask, _enc

def run():
    matrix = 'Au_mK34WFOsjNOlnet{<=Y*DZ )$e1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
