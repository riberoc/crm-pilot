import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 995) - 551
    _mask = _data(313, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'K1:)+)TN-=#iptUPvG*([O[[g<ayJ{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
