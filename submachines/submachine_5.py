import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 202) - 195
    _mask = _data(444, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'w6WiL;N#(Mx#{B:NpH%P.2q=- 6@Wr'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
