class Vec(list):
    def sum(self):
        return sum(self)


result = Vec([10, 20, 30]).sum()


print(result)