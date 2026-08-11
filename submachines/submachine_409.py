import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 144) - 609
    _mask = _data(512, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = '4$f/!] C[&eG,^p}xv+R!nWTr^H.UB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
