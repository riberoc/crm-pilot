import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 189) - 371
    _mask = _data(302, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = '0)+]B0@oQcOBiDenZR4DoR<:jv49 ='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
