import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 798) - 179
    _mask = _data(690, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = '<Hg:dUZ#2.R 2oR.()#;qH;*>`,zA<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
