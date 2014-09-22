# coding=utf-8
import datetime
import random

# 配置
day_map = {
    # 开始日期
    'start_date': datetime.datetime.strptime('9-22', '%m-%d'),
    # 0表示不刷1表示刷，从开始日期开始上下午循环
    'is_vote': '101010',
}

# 上午下午上班开始时间
vote_start_time = [datetime.datetime.strptime('06:00', '%H:%M'), datetime.datetime.strptime('13:30', '%H:%M')]

# 计算需要刷多少天
day_len = len(day_map['is_vote']) / 2

# 需要刷的半天次数
vote_half_day = 0
for vote_half in day_map['is_vote']:
    vote_half_day += int(vote_half)
# 半天投票次数
vote_times = int(32/vote_half_day)
if 6 < vote_times:
    vote_times = 6

# 已刷的次数
has_vote_nums = 1

print 'name: njgjjt'
print 'version: 1'
print 'cron:'

for day in range(day_len):
    # 当天上下午是否要刷，长度2，morning_after[0]为上午，morning_after[1]为下午
    morning_after_flag = day_map['is_vote'][day * 2: day * 2 + 2]
    # 投票日期
    vote_date = day_map['start_date']
    # 循环上下午
    for m_a in range(2):
        if '1' == morning_after_flag[m_a]:
            vote_date_str = vote_date.strftime('%m-%d').split('-')
            month_str = vote_date_str[0]
            day_str = vote_date_str[1]
            start_time = vote_start_time[m_a]
            for index in range(vote_times):
                if 0 == index:
                    # 上班开始时间随即增加1~10分钟
                    date_min_plus = datetime.timedelta(minutes=random.randint(1, 10))
                else:
                    date_min_plus = datetime.timedelta(minutes=random.randint(31, 60))
                start_time += date_min_plus
                start_time_str = start_time.strftime('%H:%M').split(':')
                hour_str = start_time_str[0]
                min_str = start_time_str[1]
                print '    - description: %s-%s %s:%s' % (month_str, day_str, hour_str, min_str)
                print '      url: %s' % ('/' * has_vote_nums)
                print '      schedule: %s %s %s %s *' % (str(int(min_str)), str(int(hour_str)), str(int(day_str)), str(int(month_str)))
                has_vote_nums += 1
    date_day_plus1 = datetime.timedelta(days=1)
    day_map['start_date'] += date_day_plus1