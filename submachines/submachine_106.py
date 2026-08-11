import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 842) - 772
    _mask = _data(199, None)
    _enc = 133
    return _mask, _enc

def run():
    matrix = 'z_y9_Oz~?7?*Lx@Hv3>v](^2sp,ARM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
