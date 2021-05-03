# TODO 데이터 종류들에 각 확률을 지정해서 샘플링한다.

import numpy as np

class RandomSampler:
    def __init__(self, catagory: list, num_sample: int, probability: list):
        """
        :param catagory: 고유의 종류  ex) ['Windows', 'Linux', 'Darwin']
        :param num_sample: 샘플링할 갯수
        :param probability: 각각의 확률
        """
        self.catagory = catagory
        self.num_sample = num_sample
        self.probability = probability

        self.sample_array = np.random.choice(self.catagory, self.num_sample, p=self.probability)


    def get_array(self):
        return self.sample_array

# 예를 들어, 옷 종류 ('상의', '하의', '아우터')를 골고루 샘플링 해야 한다.

# 카테고리는 '옷 종류' -> '