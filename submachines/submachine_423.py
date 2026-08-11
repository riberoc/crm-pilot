import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 210) - 656
    _mask = _data(958, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = '`6eRjUCPBI{^KT @u>SGShM=sMI=LA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
