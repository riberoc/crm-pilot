import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 513) - 229
    _mask = _data(892, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'VVq.&}0Am|A.m!XJ+)vLf{2Z8Pt Tq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
