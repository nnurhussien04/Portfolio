
/*Variables*/
console.log('Hello World');
let test = 'Test';
console.log(test);

let Fail = "Fail";
let Success = "Success"; 
console.log(Fail,Success);

let ChangedNo = 0.5;
ChangedNo = 1;
console.log(ChangedNo);

/*Constants*/
const FinalNo = 1;
console.log(FinalNo);

/*Primitive Types*/
let String = "String"
let Number = 5;
let Boolean = true;
let Undefined1 = undefined;
let Null = null;

/*Dynamic Type*/
console.log(typeof String);
String = 3
console.log(typeof String)

/*Objects*/

let ProgramLanguage = {
    Java:"Script",
    Version: 2.0
};
console.log(ProgramLanguage);

ProgramLanguage.Java = "Development Kit"
console.log(ProgramLanguage.Java)

ProgramLanguage['Version'] = 2.1;
console.log(ProgramLanguage.Version);

let Update = 'Version';
ProgramLanguage[Update] = 2.2;
console.log(ProgramLanguage.Version);

/*Arrays*/
let FrontEndDevelopment = ['HTML','CSS','JS','Node','Angular','React'];
console.log(FrontEndDevelopment);
console.log(FrontEndDevelopment[3])
FrontEndDevelopment[6] = 'SCSS'; 
console.log(FrontEndDevelopment);
console.log(typeof FrontEndDevelopment);
console.log(FrontEndDevelopment.length);

/*Functions*/
function greet(name,secondname){
    console.log('Yo ' + name + ' ' + secondname);
}

greet('Nebil','Nurhussien');
greet('Muhammad','Ali');

function square(number){
    return number * number;
}

console.log((square(2)));


