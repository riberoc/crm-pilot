import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 803) - 591
    _mask = _data(395, None)
    _enc = 68
    return _mask, _enc

def run():
    matrix = ',0WeEU-xjP2Cfz3g/Mt?Uf[7vZ{cn '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
