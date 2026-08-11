import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 998) - 468
    _mask = _data(292, None)
    _enc = 249
    return _mask, _enc

def run():
    matrix = 'x^ME>g.kil<nEp^GE9}H;(~ 3XTmU*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
