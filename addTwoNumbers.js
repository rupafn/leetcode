/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
     num1 = convertToarr(l1);
    num2 = convertToarr(l2);
    ans = doaddition(num1,num2);
    console.log(ans);
    var i = 1,temp;
    linklist = new ListNode(parseInt(ans[0]));
     while(i<ans.length){
      temp = new ListNode(parseInt(ans[i]));
      temp.next = linklist;
      linklist = temp;
      i++;
    }

    return linklist ;

};


function doaddition(num1, num2){
    var max = num1.length;
    var arr= new Array();
    if(num1.length<num2.length){
      max = num2.length;
    }
    i = 0;
    var carry = 0;
    while(i<max){
      let total = 0
      if(i>num1.length-1) {total = num2[i]+carry;}
      else if(i>num2.length-1) { total = num1[i]+carry;}
      else {total = num1[i]+num2[i]+carry;}
      carry =0;
      if (total>=10){

        total = total.toString();

        total = total.split("");

        carry = parseInt(total[0]);

        total = parseInt(total[1]);

      }
      arr.push(total);
      i++;
    }

    if(carry>0){
      arr.push(carry);
    }
    if(arr.length>1 && arr[arr.length-1] ==0){ arr.pop();}
    return arr.reverse();
}

function convertToarr(node){
  var arr = [];
  var num ="";
  var temp = node.next;
  var current = node.val;

  while(current>=0){

          arr.push(current);
          if(!temp){
            break;
          }
          current = temp.val;
          temp = temp.next;
  }

    return arr;
}
