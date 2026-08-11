import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 610) - 177
    _mask = _data(797, None)
    _enc = 212
    return _mask, _enc

def run():
    matrix = 'F4`k^k%>^=B{-6Vn>ZB+|tH|9.r4(E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
