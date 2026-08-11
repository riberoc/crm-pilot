import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 260) - 270
    _mask = _data(43, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = '6;<!Heb.4}evPrt#{|q~W5Y^w,Nhm['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
