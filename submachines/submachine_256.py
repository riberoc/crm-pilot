import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 985) - 641
    _mask = _data(372, None)
    _enc = 55
    return _mask, _enc

def run():
    matrix = '+m/a3o`d}#}N$Eu)S8xW.=^^Oo8rfi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
