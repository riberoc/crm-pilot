import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 333) - 371
    _mask = _data(237, None)
    _enc = 63
    return _mask, _enc

def run():
    matrix = ')|bnTx/.{CJ^`b7}h+fHHFl~#tpZrX'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
