


var reverse = function(x) {
  
  if(x>Math.pow(2,32)|| x<-Math.pow(2,32))return 0;
    let tmp = x;
    if(x<0){
      x*=-1
    }
    let strOfInt = x.toString();
    let reversed = parseInt(strOfInt.split("").reverse().join(""));
    if(tmp<0){
      reversed*=-1;
    }
    return reversed;
};


console.log(reverse(123));;
