import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 825) - 636
    _mask = _data(20, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = ']tH1(TT`: b^OldC!dP/dX?s6W32h/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
