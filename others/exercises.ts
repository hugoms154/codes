// Exercise 1: Simple Calculator Create a calculator that takes two numbers and an operator (+, -, *, /) and returns the result of the operation. 
type Operations = "+" | "-" | "*" | "/";
function calculator (first: number, second: number, operation: Operations): number {
  const operationMap: Record<Operations, (firstNum: number, secondNum: number) => number> = {
    "*": (firstNum: number, secondNum: number) => firstNum * secondNum,
    "+": (firstNum: number, secondNum: number) => firstNum + secondNum,
    "-": (firstNum: number, secondNum: number) => firstNum - secondNum,
    "/": (firstNum: number, secondNum: number) => firstNum / secondNum,
  }
  return operationMap[operation](first, second);
}

console.log("Exercise 1:");
console.log(`2 + 2 = ${calculator(2,2, '+')}`);
console.log(`2 - 2 = ${calculator(2,2, '-')}`);
console.log(`2 * 4 = ${calculator(2,2, '*')}`);
console.log(`16 / 2 = ${calculator(2,2, '/')}`);
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 2: Prime Numbers Write a function that checks whether a number is prime or not. Then create a program that prints the first 10 prime numbers. 
function isPrimeNumber(value: number): boolean {
  if (value < 2) {
    return false;
  }
  for (let i = 2; i < value; i++) {
    if (value % i == 0) {
        return false;
    }
  }
  return true;
}

function calculateFirst10PrimeNumbers() {
    let currentValue = 0;
    let primeNumbers: number[] = [];
    do {
        if(isPrimeNumber(currentValue)) {
            primeNumbers.push(currentValue);
        }
        currentValue++;
    } while (primeNumbers.length < 10);


    return primeNumbers;
}

console.log("Exercise 2:")
console.log(`number 10 is prime? ${isPrimeNumber(10)}`)
console.log(`number 13 is prime? ${isPrimeNumber(13)}`)

console.log(`First 10 prime numbers\n${calculateFirst10PrimeNumbers()}`);
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 3: Factorial Write a function to calculate the factorial of a number. Next, create a program that allows the user to enter a number and displays the corresponding factorial. 
function calculateFactorial(value: number): number {
  let factorial = 0;
  
  if (value<=0 || !Number.isInteger(value)) {
    throw Error(`could not calculate factorial of ${value}\nRules: Must be a integer higher than 0`)
  }
  for(let i = value; i > 1; i--) {
    if(factorial === 0) {
      factorial = i;
      continue;
    }
    factorial *= i
  }
  return factorial;
}

console.log("Exercise 3:");
console.log(`Factorial\n${calculateFactorial(5)}`);

console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 4: Palindrome Create a function that checks whether a word is a palindrome (that is, whether it reads the same backwards and forwards). The program must ask the user for a word and inform whether or not it is a palindrome. 
function isPalindrome(word: string): boolean {
  const reversedWord = word.split('').reverse().join('');
  return reversedWord.toLowerCase() === word.toLowerCase();
}

console.log("Exercise 4:");
console.log(`(implementation 1): is "anna" a palindrome? \n${isPalindrome("anna")}`);
console.log(`(implementation 1): is "banana" a palindrome? \n${isPalindrome("banana")}`);

function isPalindromeV2(word: string): boolean {
  let reversedWord = "";
  for(let i = word.length - 1; i >= 0; i--) {
    reversedWord += word[i];
  }
  return reversedWord.toLowerCase() === word.toLocaleLowerCase();
}

console.log(`(implementation 2): is "anna" a palindrome? \n${isPalindromeV2("anna")}`);
console.log(`(implementation 2): is "banana" a palindrome? \n${isPalindromeV2("banana")}`);
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 5: Table Create a program that receives a number from the user and displays the table of that number, from 1 to 10.
type NumberTable = {operation: `${number} x ${number}`, result: number};
function createNumberTable(value: number): NumberTable[] {
  const numberTable: NumberTable[]  = [];
  for(let i = 1; i <= 10; i++) {
    numberTable.push({operation: `${value} x ${i}`, result: value*i})
  }
  return numberTable;
}


console.log("Exercise 5:");
console.log(`Table of number 8`);
console.table(createNumberTable(8))
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 6: Vowel Counter Create a function that counts the number of vowels in a string. 
// The program should ask the user for a sentence and display how many vowels it has.
function vowelCounter(phrase: string) {
  const vowels = ["a", "e", "i", "o", "u"];
  let vowelCounter = 0;
  const lowerPhrase = phrase.toLowerCase();
  for(let i = 0; i < lowerPhrase.length; i++) {
    const isVowel = vowels.includes(lowerPhrase[i]);
    if(isVowel){
      vowelCounter++;
    }
  }
  return vowelCounter;
}

console.log("Exercise 6:")
console.log(`how many vowels in this sentence? \n${vowelCounter("how many vowels in this sentence?")}`);
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 7: Grade Average Create a program that takes a student's grades in three different subjects and calculates the average of the grades.
// Then display the calculated average.
function studentAverage(subjectGradeOne: number, subjectGradeTwo: number, subjectGradeThree: number ): number {
  const averageGrade = (subjectGradeOne + subjectGradeTwo + subjectGradeThree) / 3;
  return Number(averageGrade.toFixed(2))
}

console.log("Exercise 7:")
console.log(`Average grade in three subjects: 2,4,8 \n${studentAverage(2,4,8)}`);
console.log("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

// Exercise 8: Interest Calculation Create a function that calculates the final value of an investment based on initial capital, 
// interest rate, and investment time (in months). The program must prompt the user for these values and display the final value.
type CalculateInvestmentFinalAmount = { capital: number; rate: number; period: number; }
function calculateInvestmentFinalAmount({ capital, rate, period }: CalculateInvestmentFinalAmount) {
  const finalValue = capital*(1+rate/100)**period;
  return Number(finalValue.toFixed(2))
}

console.log("Exercise 8:")
console.log(`final value in an investment with the following rate: 10% p.m.; in period of 3 months; with capital of $10,000.00 is: ${calculateInvestmentFinalAmount({capital: 10000, period: 3, rate: 10})}`);