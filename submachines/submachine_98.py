import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 905) - 279
    _mask = _data(603, None)
    _enc = 176
    return _mask, _enc

def run():
    matrix = 'dxSVj-ddr%p -jk4^rB_Z6X5(NfW%0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
