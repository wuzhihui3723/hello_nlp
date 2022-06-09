i = float(input('请输入企业当月的利润（万元）：'))
if i <= 10:
    total_money = 0.1 * i
elif i > 10 or i <= 20:
    total_money = 0.1 * 10 + 0.075 * (i - 10)
elif i > 20 or i <= 40:
    total_money = 0.1 * 10 + 0.075 * 20 + 0.05 * (i - 20)
elif i > 40 or i <= 60:
    total_money = 0.1 * 10 + 0.075 * 20 + 0.05 * 40 + 0.03 * (i - 40)
elif i > 60 or i <= 100:
    total_money = 0.1 * 10 + 0.075 * 20 + 0.05 * 40 + 0.03 * 60 + 0.015 * (i - 60)
else:
    total_money = 0.1 * 10 + 0.075 * 20 + 0.05 * 40 + 0.03 * 60 + 0.015 * 60 + 0.01 * (i - 100)
print('当利润是{}万元的时候，应该发放的奖金总数是{}万元'.format(i, total_money))