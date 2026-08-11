import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 923) - 785
    _mask = _data(166, None)
    _enc = 60
    return _mask, _enc

def run():
    matrix = 'bu98Qk1e]PCB+b>O y8KbD3>J}AcbV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
