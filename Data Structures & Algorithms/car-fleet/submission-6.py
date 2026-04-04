class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = []

        for position, speed in zip(positions, speeds):
            cars.append((position, (target - position) / speed))

        cars = sorted(cars)

        result = 0

        while cars:
            if len(cars) == 1:
                result += 1
                cars.pop()
            elif cars[-1][1] >= cars[-2][1]:
                cars[-1] = cars.pop()
            else:
                result += 1
                cars.pop()

        return result


