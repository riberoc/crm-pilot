import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 118) - 550
    _mask = _data(554, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'qL |x=_QYT#&nb;]s0A&M=px}`gi(_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
