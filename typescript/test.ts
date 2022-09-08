// const taskA = new Promise((resolve, reject) => {
//     setTimeout(() => {
//       resolve("A");
//     }, 1);
//     setTimeout(() => {
//         reject(new Error("Crash"));
//     }, 2);
//   });
// const taskB = new Promise<string> ((resolve, reject) => {
//     setTimeout(() => {
//         resolve("B");
//     }, 2000);
//     });
// const taskC = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve("C");
//     }, 1);
//     });


// async function run () {
//     const outputA = taskA;
//     const outputB = taskB;
//     const outputC = taskC;
//     console.log(outputA);
//     console.log(outputB);
//     console.log(outputC);
// }

// run();
// console.log("HOI!");


const thisHasError = () => {
    throw new Error("BRUH");
  };
  
try {
console.log("Start process...");
thisHasError();
console.log("End process...");
} catch (error) {
if (error instanceof Error) {
    console.log(error.message);
}
} finally {
console.log("Finally");
}
