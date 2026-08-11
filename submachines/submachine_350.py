import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 314) - 555
    _mask = _data(986, None)
    _enc = 160
    return _mask, _enc

def run():
    matrix = ';<EqTUQ]v#>WXoTBq*$]Y D%*!S<){'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
