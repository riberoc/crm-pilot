import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 374) - 571
    _mask = _data(902, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = '0~}16^qiDbPKQc 0nhJc.f9%A;$sPq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
