def lengthOfLIS(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i]<dp[j]+1:
		   #如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
           #这个比max(dp[i],dp[j]+1)算的更快一点
                dp[i] =dp[j] + 1
    return max(dp)