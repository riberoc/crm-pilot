import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 165) - 122
    _mask = _data(394, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = ')[?6Yz{Mx@#Ah5zdA@ i4qimp*MeXb'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
