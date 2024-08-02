#RTO:retransmission timeout value(再送信タイムアウト値)

#EWMA:セグメントが送信されてからACKを受信するまでの時間を測定し
#最近の集計値に重み付けをして平均値を求める

#RTO:EWMAに少しの時間を上乗せした値をタイムアウト値にする

#RTT(Round Trip Time);往復遅延時間

#SampleRTT:セグメントが送信されてからACKを受信するまでの時間を測った値

#DevRTT:RTTの変動値

#EstimatedRTT(推定RTT):最新のSampleRTT値に加重をかけた
#複数のSampleRTT値からなる加重平均値
#これがEWMA

#EstimatedRTT(tn) = (1-alpha)×EstimatedRTT(tn-1)+alpha×SampleRTT(tn)
#tn : n番目のSample RTTが得られた時刻
#tn-1 : n-1番目のSample RITが帰られた時刻

#DevRTT(in) = (1-beta)DevRTT(tn-1)+beta×SampleRTT(tn)-EstimatedRTT(tn-1)｝

#RTO(tn) = EstimatedRTT(tn) + 4 × DevRTT(tn)