import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 391) - 122
    _mask = _data(283, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = "QRu&]f3[HyaT7MSjahNInH'g.w_,~<"
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
