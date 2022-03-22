1. Fixing the errors:
The program was doing inp3 - (inp1 + inp2) instead of (inp1 + inp2) - inp3.
Fixed
inp
sta 99
inp
add 99
sta 99
inp
sta 98
lda 99
sub 98
out
hlt

2. Writing own program:
inp
sta 99
inp
sta 98
sub 99
brp 09
lda 99
out
hlt
lda 98
out
hlt
