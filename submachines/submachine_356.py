import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 223) - 601
    _mask = _data(1012, None)
    _enc = 199
    return _mask, _enc

def run():
    matrix = 'RGX<^PnRaXN|:1kVtKkTCmtSBy#$-,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
