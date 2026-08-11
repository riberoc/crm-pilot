import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 867) - 748
    _mask = _data(45, None)
    _enc = 122
    return _mask, _enc

def run():
    matrix = '@@6FV!;wM,ca369PYN~X]LF{eCl?{|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
