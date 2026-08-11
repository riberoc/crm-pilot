import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 815) - 429
    _mask = _data(323, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = '4EY38~GJ_dpg1L|8#.}okC?7Ih5$xg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
