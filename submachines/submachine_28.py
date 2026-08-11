import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 200) - 136
    _mask = _data(446, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = '1mhv7t$]y],msrx-W)q_DX,]=?TY X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
