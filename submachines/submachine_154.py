import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 338) - 280
    _mask = _data(186, None)
    _enc = 208
    return _mask, _enc

def run():
    matrix = ' Q47*=2*Az]S<viK-k8QS}41$^|Wpi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
