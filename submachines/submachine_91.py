import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 794) - 922
    _mask = _data(1872, None)
    _enc = 171
    return _mask, _enc

def run():
    matrix = '0R5F8!L+nJCrx[1z_qY^w{?_cB| !.'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
