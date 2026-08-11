import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 977) - 644
    _mask = _data(252, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '6K:Q9;yy)JD1+*_{5gM esnWkELpuD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
