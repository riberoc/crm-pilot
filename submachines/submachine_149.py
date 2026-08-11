import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 588) - 646
    _mask = _data(155, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = '{^(88evw-5~*s~]R6trJX F-qf,L>`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
