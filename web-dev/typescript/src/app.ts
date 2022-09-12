const greet: string = "Hello, Thinc!";
console.log(greet);

async function getData(){
    const response = await fetch("https://firstact-api.thinc.in.th/courses");
    const data = await response.json();

    return data;
}

console.log(getData());