import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 923) - 864
    _mask = _data(86, None)
    _enc = 118
    return _mask, _enc

def run():
    matrix = '&GkPMEnS^!$C)E60Ft(5NsDl.MK.QJ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
