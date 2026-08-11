import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 732) - 486
    _mask = _data(74, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'k -&i{zFLFXfr%9F}m-QS+X7kH:>T_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
