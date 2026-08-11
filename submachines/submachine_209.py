import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 745) - 144
    _mask = _data(991, None)
    _enc = 175
    return _mask, _enc

def run():
    matrix = '?d._jb`&1 g~g&W|<$DT#&(^.~b.?2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
