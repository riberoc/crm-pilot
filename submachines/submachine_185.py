import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 696) - 608
    _mask = _data(445, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = ' +[z[)MVmm<L$Ahcw(Q6g(LI]SbUDa'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
