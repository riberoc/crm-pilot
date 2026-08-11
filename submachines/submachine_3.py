import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 409) - 362
    _mask = _data(67, None)
    _enc = 119
    return _mask, _enc

def run():
    matrix = '8%}S<Ghuk|[uM14IEml`0U!F}8)reO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
