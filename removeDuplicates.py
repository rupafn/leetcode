def removeDuplicates(self, nums):
    x = {};
    ans = [];
    for i in nums:
        if i not in x:
            x[i] = i;
            ans.append(i);
    return ans;

removeDuplicates('t',[0,0,1,1,1,2,2,3,3,4])
