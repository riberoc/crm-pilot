import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 905) - 860
    _mask = _data(245, None)
    _enc = 51
    return _mask, _enc

def run():
    matrix = 'gW$ZcIkB6POjk?y}7(osVT>yVcJK~2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
