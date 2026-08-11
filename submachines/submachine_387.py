import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 757) - 455
    _mask = _data(162, None)
    _enc = 159
    return _mask, _enc

def run():
    matrix = '-BP/n>fzfN6VC~v _ZlSNAMeNgaNy%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
