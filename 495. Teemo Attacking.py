class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        loss_hp = 0
        for i in range(len(timeSeries)-1):
            if (timeSeries[i+1]-timeSeries[i])>duration:
                loss_hp += duration
            else:
                loss_hp += (timeSeries[i+1]-timeSeries[i])
        if timeSeries:
            return loss_hp+duration
        else:
            return loss_hp
