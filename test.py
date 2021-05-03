from RandomSampler import RandomSampler
import collections

# 카테고리 정의
catagory_list = ['상의', '하의', '아우터']

# 샘플링할 개수
num_sample = 100

# 각각의 확률
prob = [0.25, 0.45, 0.3]

if __name__ == '__main__':
    random_sampler =  RandomSampler(catagory_list, num_sample, prob)

    sample_result = random_sampler.get_array()
    # print(sorted(collections.Counter(sample_result).items(), key=lambda x: x[0]))
    print(collections.Counter(sample_result))