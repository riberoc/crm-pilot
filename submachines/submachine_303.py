import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 325) - 678
    _mask = _data(617, None)
    _enc = 151
    return _mask, _enc

def run():
    matrix = '#UIJtl2oMu|2*!x.y xH,7*u_0aM]6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
