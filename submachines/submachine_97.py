import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 581) - 469
    _mask = _data(63, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = 'p46Y)u<4q*<aGuY041IizHNfyBr4_:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
