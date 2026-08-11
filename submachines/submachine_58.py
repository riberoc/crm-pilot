import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 892) - 229
    _mask = _data(761, None)
    _enc = 179
    return _mask, _enc

def run():
    matrix = '6up3T[Q)--g.!1}%n2a GXM@rL*<wD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
