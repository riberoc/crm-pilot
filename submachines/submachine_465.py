import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 298) - 488
    _mask = _data(940, None)
    _enc = 156
    return _mask, _enc

def run():
    matrix = 'J% ?c?The?ibf$!^`b@i.&YXz^yD5w'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
