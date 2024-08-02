# rtt: SampleRTT
# ertt: EstimatedRTT (EWMA)
# devrtt: devRTT
# rto: RTO

alpha = 0.125
beta = 0.25

rtt_lst = [10, 12, 7, 8, 15, 20, 17, 24]

ertt = rtt_lst[0]
devrtt = ertt / 2
rto = ertt + 4 * devrtt

for i, rtt in enumerate(rtt_lst[1:], start=2):
    devrtt = (1 - beta) * devrtt + beta * abs(rtt - ertt)
    ertt = (1 - alpha) * ertt + alpha * rtt
    rto = ertt + 4 * devrtt
    print('i={}, rtt={}, ertt={:.2f}, devrtt={:.2f}, rto={:.2f}'.format(i, rtt, ertt, devrtt, rto))

#i=2, rtt=12, ertt=10.25, devrtt=4.25, rto=27.25
#i=3, rtt=7, ertt=9.84, devrtt=4.00, rto=25.84
#i=4, rtt=8, ertt=9.61, devrtt=3.46, rto=23.46
#i=5, rtt=15, ertt=10.29, devrtt=3.94, rto=26.06
#i=6, rtt=20, ertt=11.50, devrtt=5.39, rto=33.04
#i=7, rtt=17, ertt=12.19, devrtt=5.41, rto=33.84
#i=8, rtt=24, ertt=13.66, devrtt=7.01, rto=41.72