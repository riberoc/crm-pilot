import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 322) - 409
    _mask = _data(162, None)
    _enc = 81
    return _mask, _enc

def run():
    matrix = 'VPV4HWEPVAmLax;6UDOIP- X3=mOGx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
