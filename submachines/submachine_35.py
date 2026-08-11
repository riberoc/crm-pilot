import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 789) - 763
    _mask = _data(123, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'iYz6Ah {I~skm2eRQyj(KA@Mxq&`kS'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
