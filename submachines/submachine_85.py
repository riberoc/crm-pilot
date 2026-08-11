import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 800) - 588
    _mask = _data(17, None)
    _enc = 255
    return _mask, _enc

def run():
    matrix = 'wf<E<QCmU-8DM](%oWtu9J&Zt4T>;b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
