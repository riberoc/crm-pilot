import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 258) - 651
    _mask = _data(524, None)
    _enc = 151
    return _mask, _enc

def run():
    matrix = '[XNuryc1er,~MKTaBrG4 }L_v{lO*0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
