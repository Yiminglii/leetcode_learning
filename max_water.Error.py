#这段代码的测试平台在leecode ,最多盛水问题 其中测试[1,1]无法通过

class Solution:
    def maxArea(self, height: List[int]) -> int:
        a,v_max=0,0
        rear_l=0
        list_len=len(height)
        rear_r=list_len-1
        r=rear_r-rear_l
        v_max=min(height[0],height[list_len-1])*list_len
        while r>0:
            a=min(height[rear_l],height[rear_r])*(rear_r-rear_l)
            v_max=max(a,v_max)
            if(height[rear_l]>height[rear_r]):
                rear_r=rear_r-1
            else:
                rear_l=rear_l+1
            r=rear_r-rear_l
        return v_max

#最后一次修改：2020 9 29