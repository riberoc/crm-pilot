import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 622) - 188
    _mask = _data(788, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'Id: l~V7^x.Cb#*cNaKCl`882Ek<y?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
