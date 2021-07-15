// MULTIPLES OF 3 AND 5:
function multiples() {
  let sum = 0,
      upperLimit = document.getElementById("multiples").value;

  for (let i = 1; i < upperLimit; i++) {
    if ((i % 3 === 0) || (i % 5 === 0)) {
      sum += i;
    }
  }
  //Display results:
  document.getElementById("multi-sum").innerText = sum;
}
// FIBONACCI:
function fibonacci() {
  let sequence = [1,2], // start the fibonacci seq -> [x,y] for reference
      seqIndex = 1, // position of last number
      posX = 0, // position for the addition
      posY = 1, // position for the addition
      upperLimit = document.getElementById("fibo").value,
      sum = 0;
  //generate the sequence with user defined upper limit:
  do  {
    seqIndex++;
    sequence[seqIndex] = (sequence[posX] + sequence[posY]);
    posX++;
    posY++;
  } while (sequence[seqIndex] < upperLimit);
  //add even-valued terms from sequence:
  for (let index = 0; index < sequence.length; index++) {
    if (sequence[index] % 2 === 0 && sequence[index] < upperLimit) {
      sum += sequence[index];
    }
  }
  // Display results:
  document.getElementById("fibo-sum").innerText = sum;
}
//  LARGEST PRIME:
function largestPrime() {
  let dividend = document.getElementById("toFactor").value,
      divisor = 2,
      lp = 0;

  if (dividend < 2 )
    return document.getElementById("lgPrime").innerText = 1;

  do {
    if (dividend % divisor === 0) {
        dividend = dividend/divisor;
        lp = divisor;
        divisor = 2;
    }
    else {
        divisor++;
    }

  } while (dividend !== 1);
  document.getElementById("lgPrime").innerText = lp;
}
