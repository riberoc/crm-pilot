import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 190) - 151
    _mask = _data(440, None)
    _enc = 110
    return _mask, _enc

def run():
    matrix = 'RE3q/mZ@LGjFWVsC[VTuid6.33z!?D'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
