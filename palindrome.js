
var reverseString = function(str){
    let i = str.length-1;
    let strnew ="";
    for(i = str.length-1 ; i>=0; i--){
      strnew+=str[i];
    }
    return strnew;
}

var isPalindrome = function(x) {
   let strOfInt = x.toString();
   let reverseStrOfInt = reverseString(strOfInt);
   if(reverseStrOfInt == strOfInt){
     console.log(reverseStrOfInt);
     console.log(strOfInt);
   }
   // console.log(reverseStrOfInt);
};



isPalindrome(111);
