import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 284) - 550
    _mask = _data(995, None)
    _enc = 192
    return _mask, _enc

def run():
    matrix = 'p)|a?MX(!Hw#yewbz`^&iQ{QJ Ck(^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
