import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 891) - 296
    _mask = _data(539, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = ':VZG3F_~]~dS ^)A>XFYF(fzZB)M4,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
