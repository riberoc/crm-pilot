import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 304) - 580
    _mask = _data(922, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'YT+T~GEZ;U9:%g bdwEQVj_tK?mMg^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
