/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let map = new Array();
    let max = 0;
    let i =0;
    let len = s.length;
    if(len == 0) return 0;
    if(len == 1) return 1;
    for(i=0; i<len; i++) {
      if(map.indexOf(s[i],start)>-1) {
        temp = start;
        start =  map.indexOf(s[i],start)+1;
      }
      max = Math.max(max,i+1-start);
      map.push(s[i]);

    }

    return max;
};
