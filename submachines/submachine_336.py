import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 848) - 871
    _mask = _data(1796, None)
    _enc = 238
    return _mask, _enc

def run():
    matrix = '2`0m!O_yVqf<shlC0E?a_Cu.i[Ab+@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
