


var reverse = function(x) {
    if(x>)
    var reverse = 0;
    var neg = false;
    if(x<1){
      neg = true;
      x = Math.abs(x);


    }
    while(x>0 ){
      remainder = x %10;
      reverse = (reverse*10)+remainder;
      x = Math.floor(x/10);
    }
  if(reverse>2147483647) return 0;
  if(neg){
    reverse = -Math.abs(reverse);
  }
  return reverse;
};


reverse(120);;
