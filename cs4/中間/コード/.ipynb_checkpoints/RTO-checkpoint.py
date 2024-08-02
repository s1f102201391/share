# TCPの再送タイムアウト（RTO）を計算するための関数を定義

def calculate_rto(sample_rtts, alpha=0.125, beta=0.25):
    # 最初のSampleRTTを基に初期値を設定
    estimated_rtt = sample_rtts[0]
    dev_rtt = sample_rtts[0] / 2

    # SampleRTTのリストをループして、EstimatedRTTとDevRTTを更新
    for sample_rtt in sample_rtts[1:]:
        estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sample_rtt
        dev_rtt = (1 - beta) * dev_rtt + beta * abs(sample_rtt - estimated_rtt)

    # RTOを計算
    rto = estimated_rtt + 4 * dev_rtt
    return estimated_rtt, dev_rtt, rto

# 与えられたSampleRTTのリスト
sample_rtts = [10, 12, 7, 8, 15, 20, 17, 24]

# RTOを計算
estimated_rtt_t8, dev_rtt_t8, rto_t8 = calculate_rto(sample_rtts)

print(f"EstimatedRTT at time t8: {estimated_rtt_t8} ms")
print(f"DevRTT at time t8: {dev_rtt_t8} ms")
print(f"RTO at time t8: {rto_t8} ms")
