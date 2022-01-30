def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



# s,t: a*s + b*t = gcd(a,b)
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r # ie. a, b = b, a % b
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t # Bézout coefficients



if __name__=="__main__":
    a = 26513
    b = 32321
    u,v = extended_gcd(a, b)
    