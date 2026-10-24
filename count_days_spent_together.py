class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31]

        def convert(date):
            month, day = map(int, date.split('-'))

            total = day

            for i in range(month - 1):
                total += days_in_month[i]

            return total

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        if start > end:
            return 0

        return end - start + 1   
