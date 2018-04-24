# -*- coding: utf-8 -*-


class Picker(object):
    def __init__(self, p, batches=None):
        self.p = p
        self.batches = batches

    def swap(self, picker, i, j):
        self.batches[i], picker.batches[j] = picker.batches[j], self.batches[i]

    def shift(self, picker, i, j):
        picker.batches.insert(j, self.batches[i])
        del self.batches[i]

    def tune(self):
        if self.batches:
            self.batches[0].b = 0
            self.batches[0].sd = 0
            j = 1
            for batch in self.batches[1:]:
                prev = self.batches[j - 1]
                batch.sd = prev.sd + prev.pt
                batch.b = j
                j += 1
        # if i == 0:
        #     j = 1
        #     self.batches[0].sd = 0
        #     for batch in self.batches[1:]:
        #         prev = self.batches[j-1]
        #         batch.sd = prev.sd + prev.pt
        #         j += 1
        # else:
        #     j = i
        #     for batch in self.batches[i:]:
        #         prev = self.batches[j-1]
        #         batch.sd = prev.sd + prev.pt
        #         j += 1

    def get_batch_centers(self, df_items):
        batch_centers = []
        for batch in self.batches:
            batch_centers.append(batch.get_center(df_items))
        return batch_centers

    def get_batch_available(self, c):
        weights = []
        for batch in self.batches:
            weights.append(c - batch.weight)
        return weights

    def re_routing(self, df_items):
        for i, batch in enumerate(self.batches):
            if batch.weight == 0:
                del self.batches[i]
        j = 1
        self.batches[0].b = 0
        self.batches[0].routing_time(df_items, para='s')
        # self.batches[0]._routing(df_items)
        for batch in self.batches[1:]:
            batch.routing_time(df_items, para='s')
            # batch._routing(df_items)
            prev = self.batches[j - 1]
            batch.sd = prev.sd + prev.pt
            batch.b = j
            j += 1

