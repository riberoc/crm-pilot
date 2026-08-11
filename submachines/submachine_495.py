import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 392) - 744
    _mask = _data(661, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = 'mk^5%Bs*p9w_U27DpkB?2-Wxuoy8 %'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
