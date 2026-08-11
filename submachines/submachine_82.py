import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 679) - 714
    _mask = _data(445, None)
    _enc = 82
    return _mask, _enc

def run():
    matrix = 'T= v@m9IyI%MV(P028(kZD_NPVP)Fq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
