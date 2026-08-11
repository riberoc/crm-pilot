import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 328) - 125
    _mask = _data(122, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = '^[K`#.[k 9=VJ1.Y0(dB9s_z{z_&qQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
