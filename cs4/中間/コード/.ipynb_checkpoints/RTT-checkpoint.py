# TCPにおけるEstimatedRTTの計算

# 与えられた値
sampleRTT = 80  # SampleRTT at time t7 in milliseconds
estimatedRTT_t6 = 120  # EstimatedRTT at time t6 in milliseconds
alpha = 0.125  # alphaの値

# EstimatedRTT at time t7の計算
estimatedRTT_t7 = (1 - alpha) * estimatedRTT_t6 + alpha * sampleRTT

# 結果を出力
print(f"EstimatedRTT(t7) = {estimatedRTT_t7} ms")
