def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = [];
        b = [];
        result = []
        if(len(nums1)<len(nums2)):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
        i = 0;
        j = 0;
        while(1):
            if(len(a)==0):
                if(len(b)>0):
                    result = result+b
                break;
            if( len(b)==0):
                if(len(a)>0):
                    result = result+a
                break;
            if a[i]<b[j]:
                result.append(a.pop(i))
            else:
                result.append(b.pop(i))

        length = len(result);
        median = 0;
        median = result[int((length-1)/2)]
        if length%2==0:
            median = (result[int(length/2)] + result[int(length/2-1)])/2

        return float(median)
