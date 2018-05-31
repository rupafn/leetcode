

var findMed = function(arr){
  if(arr.length%2 == 0){
    let ind1 = arr.length/2;
    let ind2 = ind1-1;
    let median = (arr[ind1]+arr[ind2])/2;
    return median;
  } else{
    let ind = (arr.length-1)/2;
    let median = arr[ind];
    return median;
  }
}

var reduceArr = function(arr, fInd,lInd){
  return arr.slice(fInd,lInd);
}

var findMedianSortedArrays = function(nums1, nums2) {
    var a1,a2;
    if(nums1.length>nums2.length){
      a1 = nums1; a2 = nums2;
    } else if(nums1.length<nums2.length) {
      a1 = nums2; a2 = nums1;
    } else{
      a1 = nums1; a2 = nums2;
    }
    var flag = 0;
    let med1 = findMed(a1);
    let med2 = findMed(a2);
    while(1){
      if(med1 == med2 ) break;

      if(med1>med2){
          a1 = reduceArr(a1, 0, Math.ceil(a1.length/2));
          a2 = reduceArr(a2, Math.floor(a2.length/2)-1,a2.length);
      } else if(med1<med2) {
        a2 = reduceArr(a2, 0, Math.ceil(a2.length/2));
        a1 = reduceArr(a1, Math.floor(a1.length/2)-1,a1.length);
      }
      med1 = findMed(a1);
      med2 = findMed(a2);
    }
    console.log(med1);

};

nums1 = [1,5,7,8];
nums2 = [3,5];
findMedianSortedArrays(nums1, nums2);
