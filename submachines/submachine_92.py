import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 262) - 443
    _mask = _data(793, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'Qe2okat YplWeBb_o7&GABbo:a6:K@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
