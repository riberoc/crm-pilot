import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 950) - 149
    _mask = _data(697, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = 'R) $Lk.X+{<)`}4+2K/ILzAkl=87$e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
