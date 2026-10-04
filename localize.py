from math import sqrt

def ochiai(failed_s, passed_s, total_failed):
    denom = sqrt(total_failed * (failed_s + passed_s))
    return failed_s / denom if denom else 0.0

if __name__ == "__main__":
    print(ochiai(2, 1, 2))  # 0.816
    print(ochiai(2, 8, 2))  # 0.447
    print(ochiai(0, 5, 2))  # 0.0