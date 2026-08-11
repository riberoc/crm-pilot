import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 440) - 425
    _mask = _data(126, None)
    _enc = 24
    return _mask, _enc

def run():
    matrix = "wAq[o',>hC{Ap%om]^I]-@2l+#qj2{"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
