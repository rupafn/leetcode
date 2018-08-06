

function ListNode(val) {
   this.val = val;
   this.next = null;
 }



var mergeTwoLists = function(l1, l2) {
     console.log(l1);
     var tmp = l1
    while(1){
      console.log(tmp.val);
      tmp= tmp.next;
      var val1 =tmp.val;

      if(tmp==null){
        break;
      }
    }
};

var l1 = new ListNode(1);
l1.next = new ListNode(2);
l1.next.next = new ListNode(4);

var l2 = new ListNode(1);
l2.next = new ListNode(3);
l2.next.next = new ListNode(4);
mergeTwoLists(l1,l2);
