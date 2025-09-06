////----Java script 学習レッスンⅠ----////
///----文字列と数値----///
//----1.JavaScript(ES6)を学ぼう----//
console.log("「ES6 学習コース」へようこそ！");
console.log("にんじゃわんこと一緒にES6を学んでいきましょう。");



//----2.console.log()----//
// 「Hello World」とコンソールに出力してください
console.log("Hello World");

// 「にんじゃわんこ」とコンソールに出力してください
console.log("にんじゃわんこ");

// 以下の行をコメントアウトしてください
//console.log("この行をコメントアウトしてください");



//----3.数値----//
// 5と3を足した値を出力してください
console.log(5+3);

// 20から8を引いた値を出力してください
console.log(20-8);

// "4 + 5" を文字列として出力してください
console.log("4+5");



//----4.掛け算・割り算----//
// 8と4をかけた結果を出力してください
console.log(8*4);

// 24を4で割った結果を出力してください
console.log(24/4);

// 7を2で割った余りを出力してください
console.log(7%2);



//----5.文字列の連結----//
// 「ひつじ」と「仙人」を連結してコンソールに出力してください
console.log("ひつじ" + "仙人");

// 文字列の「20」と「15」を連結してコンソールに出力してください
console.log("20" + "15");



//----6.変数----//
// 変数nameを定義し、「にんじゃわんこ」を代入してください
let name = "にんじゃわんこ";

// 変数nameの値を出力してください
console.log(name);



//----7.変数の役割----//
// 変数lengthを定義してください
let length = 5;

// 変数lengthの値を出力してください
console.log(length);

// 変数lengthを用いて、円の面積を出力してください
console.log(length * length *3);



//----8.変数の更新----//
let name = "にんじゃわんこ";
console.log(name);

// 変数nameの値を"とりずきん"に更新してください
name = "とりずきん";

// 変数nameの値を出力してください
console.log(name);



//----9.変数の値の更新----//
let number = 7;
console.log(number);

// 変数numberの値に3を加えてください
number += 3;

console.log(number);

// 変数numberの値を2で割ってください
number /= 2;

console.log(number);


//----10.定数----//
// 定数languageを定義してください
const language = "フランス語";

// 定数languageの値を出力してください
console.log(language);

// 定数languageを用いて、「〇〇を話せます」と出力してください
console.log(language + "を話せます");



//----11.テンプレートリテラル----//
const name = "にんじゃわんこ";
const age = 14;

// 「ぼくの名前は〇〇です」とコンソールに出力してください
console.log(`ぼくの名前は${name}です`);

// 「今は〇〇歳です」と出力してください
console.log(`今は${age}歳です`);



//----12.条件分岐----//
const level = 12;

// 条件式を「level > 10」とするif文を作ってください
if (level > 10) {
  console.log("レベルが10より大きいです");
}



//----13.真偽値と比較演算子(1)----//
const age = 24;

// 「age >= 20」を出力してください
  console.log(age >= 20);
// 「age < 20」を出力してください
  console.log(age < 20);


// ageの値が20以上の場合に、「私は20歳以上です」と出力してください
if(age >= 20){
  console.log("私は20歳以上です");
}



//----14.真偽値と比較演算子(2)----//
const password = "ninjawanko";

// passwordの値が"ninjawanko"の場合、「ログインに成功しました」と出力してください
if(password == "ninjawanko"){
  console.log("ログインに成功しました");
}



// passwordの値が"ninjawanko"でない場合、「パスワードが間違っています」と出力してください
if(password != "ninjawanko"){
  console.log("パスワードが間違っています");
}



//----15.else----//
const age = 17;

// 条件式が成り立たない場合に「私は20歳未満です」と出力してください
if (age >= 20) {
  console.log("私は20歳以上です");
} else{
  console.log("私は20歳未満です");
}


//----16.else if----//
const age = 17;

// ageの値が10以上20未満のとき、「私は20歳未満ですが、10歳以上です」と出力してください
if (age >= 20) {
  console.log("私は20歳以上です");
} else if(age >= 10){
  console.log("私は20歳未満ですが、10歳以上です");
} else {
  console.log("私は10歳未満です");
}


//----17.複数の条件式----//
const age = 24;

// 指定された条件のif文を作成してください
if(age >= 20 && age < 30){
  console.log("私は20代です");
}



//----18.switch文とは----//
const n = 2;

switch (n) {
  case 1:
    console.log("大吉です");
    break;

  // nの値が2のcaseを追加してください
   case 2:
     console.log("吉です");
      break;
  
  
  
  // nの値が3のcaseを追加してください
    case 3:
      console.log("小吉です");
        break;
}




//----19.switch文(2)----//
const n = 4;

switch (n) {
  case 1:
    console.log("大吉です");
    break;
  case 2:
    console.log("吉です");
    break;
  case 3:
    console.log("小吉です");
    break;
  // どのcaseにも合致しなかったときの処理を追加してください
  default:
    console.log("凶です");
      break;
}




////----Java script 学習レッスンⅡ----////
///----繰り返し処理----///
//----1.変数の復習----//
// 変数numberを定義してください
let number = 0;

// 変数numberに1を加えて、その後に変数numberの値を出力してください
number += 1;
console.log(number);


// 上述の2行のコードを4回、貼り付けてください
number += 1;
console.log(number);

number += 1;
console.log(number);

number += 1;
console.log(number);

number += 1;
console.log(number);



//----2.while文----//
// 変数numberを定義してください
let number = 1;

// while文を作成してください
while(number <= 100 ){
  console.log(number);
  number += 1;
}



//----3.for文----//
// for文を用いて、1から100までの数字を出力してください
for(let number=1; number <=100; number++){
  console.log(number);
}



//----4.繰り返し処理のまとめ----//
// for文を完成させてください
for (let number = 1; number <= 100 ; number++){
  // if文を用いて、numberが3の倍数の時に「3の倍数です」、そうでないときは数字を出力してください
  if(number%3==0){
    console.log("3の倍数です");
  }else{
    console.log(number);
  }
}


//----5.配列----//
// 定数animalsに、指定された配列を代入してください
const animals = ["dog", "cat", "sheep"];

// 定数animalsを出力して下さい
console.log(animals);


//----6.配列の要素にアクセス----//
const animals = ["dog", "cat", "sheep"];

// 配列の1つ目の要素を出力してください
console.log(animals[0]);

// 配列の3つ目の要素を出力してください
console.log(animals[2]);



//----7.配列の要素の更新----//
const animals = ["dog", "cat", "sheep"];

// 配列animalsの3つ目の要素を「rabbit」に更新してください
animals[2] = "rabbit";

// 配列animalsの3つ目の要素をコンソールに表示して下さい
console.log(animals[2]);



//----8.配列と繰り返し(1)----//
const animals = ["dog", "cat", "sheep"];

// for文を用いて、配列の値を順にコンソールに出力してください
for(let i=0; i<3; i++){
  console.log(animals[i]);
}


//----9.配列と繰り返し(2)----//
const animals = ["dog", "cat", "sheep", "rabbit", "monkey", "tiger", "bear", "elephant"];

// lengthを用いて配列の要素の数を出力してください
console.log(animals.length);

// lengthを用いて条件式を書き換えてください
for (let i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}


//----10.オブジェクトとは----//
// 定数characterを定義し、指定されたオブジェクトを代入してください
const character = {name:"にんじゃわんこ", age:14};

// characterの値を出力してください
console.log(character);



//----11.オブジェクトの値の取得・更新----//
const character = {name: "にんじゃわんこ", age: 14};

// characterのnameの値を出力してください
console.log(character.name);

// characterのageの値を「20」に更新してください
character.age = 20;

// characterをコンソールに出力してください
console.log(character);



//----12.オブジェクトを要素に持つ配列(1)----//
const characters = [
  {name: "にんじゃわんこ", age: 14},
  {name: "ひつじ仙人", age: 1000}
];

// charactersの1つ目の要素をコンソールに出力してください
console.log(characters[0]);

// charactersの2つ目の要素の「name」に対応する値をコンソールに出力してください
console.log(characters[1].name);



//----13.オブジェクトを要素に持つ配列(2)----//
const characters = [
  {name: "にんじゃわんこ", age: 14},
  {name: "ひつじ仙人", age: 100},
  {name: "ベイビーわんこ", age: 5},
];

// for文を完成させてください
for (let i = 0 ;i < characters.length ;i++) {
  console.log("--------------------");
  
  // 定数characterを定義してください
  const character = characters[i];
  
  // 「名前は〇〇です」を出力してください
  console.log("名前は" + character.name + "です");
  
  // 「〇〇歳です」を出力してください
  console.log(character.age + "歳です");
  
}



//----14.undefinedとは----//
const characters = [
  {name: "にんじゃわんこ", age: 14},
  {name: "ひつじ仙人", age: 100},
  {name: "ベイビーわんこ", age: 5},
  // 要素を追加してください
  {name: "とりずきん"}
];

for (let i = 0; i < characters.length; i++) {
  console.log("--------------------");
  
  const character = characters[i];
  
  console.log(`名前は${character.name}です`);
  console.log(`${character.age}歳です`);
}



//----15.undifinedの対応----//
const characters = [
  {name: "にんじゃわんこ", age: 14},
  {name: "ひつじ仙人", age: 100},
  {name: "ベイビーわんこ", age: 5},
  {name: "とりずきん"}
];

for (let i = 0; i < characters.length; i++) {
  console.log("--------------------");
  
  const character = characters[i];
  
  console.log(`名前は${character.name}です`);
  
  // if文を追加してください
  if(character.age == undefined){
    console.log("年齢は秘密です");
  }else{
    console.log(`${character.age}歳です`);
  }
  
}



//----16.総合演習(1)----//
const cafe = {            
name: "Progateカフェ",            
  businessHours: {             
// businessHoursの値に指定されたオブジェクトを代入してください            
    opening: "10:00(AM)",            
    closing: "8:00(PM)"            
}            
};            

// 「店名:〇〇」を出力してください            
console.log(`店名:${cafe.name}`);            

// 「営業時間：〇〇から△△」を出力してください            
console.log(`営業時間:${cafe.businessHours.opening}から${cafe.businessHours.closing}`);



//----17.総合演習(2)----//
const cafe = {
  name: "Progateカフェ",
  businessHours: { 
    opening: "10:00(AM)",
    closing: "8:00(PM)"
  },
  // menusプロパティに配列を代入してください
  menus: ["コーヒー", "紅茶", "チョコレートケーキ"]
  
};

console.log(`店名: ${cafe.name}`);
console.log(`営業時間:${cafe.businessHours.opening}から${cafe.businessHours.closing}`);
console.log(`----------------------------`);
console.log("おすすめメニューはこちら");

// for文を用いて配列menusの中身を表示させてください
for(let i = 0; i < cafe.menus.length; i++){
  console.log(cafe.menus[i]);
}




////----Java script 学習レッスンⅢ----////
///----関数----///
//----1.関数とは(1)----//
const greet = function() {
  console.log("こんにちは！");
  console.log("関数を学習していきましょう！");
};

// 関数を呼び出してください
greet();



//----2.関数とは(2)----//
// 定数helloに関数を代入してください
const hello = function(){
  console.log("こんにちは！");
  console.log("私の名前はShinです");
}

// 定数helloに代入された関数を呼び出してください
hello();



//----3.アロー関数----//
// 定数greetにアロー関数を代入してください
const greet = ()=>{
  console.log("こんにちは！");
}

// 定数greetを呼び出してください
greet();



//----4.引数----//
// 関数の引数にnameを追加してください
const greet = (name) => {
  // 「こんにちは、〇〇さん」となるように出力してください
  console.log(`こんにちは、${name}さん`);
  
};

// greetの引数に「ひつじ仙人」を渡して呼び出してください
greet("ひつじ仙人");



//----5.複数の引数----//
// 関数の引数にnumber1とnumber2を追加してください
const add = (number1, number2) => {
  // number1とnumber2を足した値をコンソールに出力してください
  console.log(number1 + number2);
};

// 引数に5と7を渡して関数を呼び出してください
add(5, 7);



//----6.戻り値----//
const half = (number) => {
  // numberを2で割った値を戻り値として返してください
  return number / 2;
};

// 定数resultを定義してください
const result = half(130);

// 「130の半分は〇〇です」となるように出力してください
console.log(`130の半分は${result}です`);



//----7.戻り値の活用----//
const check = (number) => {
  // numberが3の倍数かどうかを戻り値として返してください
  return number % 3 === 0;
  
};

// if文の条件式で、checkを呼び出してください
if (check(123)) {
  console.log("3の倍数です");
} else {
  console.log("3の倍数ではありません");
}



//----8.スコープ----//
// 関数の外側に定数nameを定義してください
const name = "ひつじ仙人";

const introduce = () => {
  // 関数の内側に定数nameを定義してください
  const name = "にんじゃわんこ";

  // 定数nameを出力してください
  console.log(name);
  
};

introduce();

// コードを貼り付けて、定数nameを出力してください。
console.log(name);



//----9.総合演習(1)----//
// toMinutes関数を定義してください
const toMinutes = (hour, minute) =>{
  return hour * 60 + minute;
}

// 定数resultに、toMinutes関数の戻り値を代入してください
const result = toMinutes(3, 20);

// 「◯◯分」となるように、分に換算した結果を出力してください
console.log(`${result} 分`);





////----Java script 学習レッスンⅣ----////
///----クラスの基本----///
//----1.オブジェクトの復習----//
// 定数animalを定義してください
const animal = {
  name : "レオ",
  age : 3,
  greet :() => {
    console.log("こんにちは");
  }
}

// animalのnameプロパティの値を出力してください
console.log(animal.name);

// animalのgreetプロパティの関数を実行してください
animal.greet();



//----2.クラスの定義----//
// Animalクラスを定義してください
class Animal{
  
}



//----3.インスタンス生成----//
class Animal {
}

// Animalクラスのインスタンスを定数animalに代入してください
const animal = new Animal();

// 定数animalの値を出力してください
console.log(animal);



//----4.コンストラクタ(1)----//
class Animal {
  // コンストラクタを追加してください
  constructor(){
    console.log("インスタンスを生成しました");
  }
  
}

const animal = new Animal();



//----5.コンストラクタ(2)----//
class Animal {
  constructor() {
    // nameの値に文字列「レオ」を代入してください
    this.name = "レオ";
    
    // ageの値に数値の「3」を代入してください
    this.age = 3;
  }
}

const animal = new Animal();

// 「名前: 〇〇」となるように出力してください
console.log(`名前: ${animal.name}`);

// 「年齢: 〇〇」となるように出力してください
console.log(`年齢: ${animal.age}`);



//----6.コンストラクタ(3)----//
class Animal {
  // 引数に「name」と「age」を追加してください
  constructor(name, age) {
    // 「"レオ"」の代わりに引数nameの値を代入してください
    this.name = name;
    
    // 「3」の代わりに引数ageの値を代入してください
    this.age = age;
  }
}

// 引数に「"モカ"」と「8」を渡してください
const animal = new Animal("モカ", 8);

console.log(`名前: ${animal.name}`);
console.log(`年齢: ${animal.age}`);



//----7.メソッド----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  // greetメソッドを追加してください
  greet(){
    console.log("こんにちは");
  }
  
}

const animal = new Animal("レオ", 3);

console.log(`名前: ${animal.name}`);
console.log(`年齢: ${animal.age}`);

// animalに対してgreetメソッドを呼び出してください
animal.greet();


//----8.メソッドとthis----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  // infoメソッドを追加してください
  info(){
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
  
}

const animal = new Animal("レオ", 3);
animal.greet();

// animalに対してinfoメソッドを呼び出してください
animal.info();



//----9.メソッド内でメソッドの呼び出し----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    // greetメソッドを呼び出してください
    this.greet();
    
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

const animal = new Animal("レオ", 3);
// 以下の1行を消してください

animal.info();



//----10.継承とは----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

// Animalクラスを継承してDogクラスを定義してください
class Dog extends Animal{
  
}


const animal = new Animal("レオ", 3);
animal.info();



//----11.継承の活用----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

class Dog extends Animal {
}

// 定数dogにDogクラスのインスタンスを代入してください
const dog = new Dog("レオ", 4);

// dogに対してinfoメソッドを呼び出してください
dog.info();



//----12.継承とメソッドの追加----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

class Dog extends Animal {
  // getHumanAgeメソッドを追加してください
  getHumanAge(){
    return this.age * 7;
  }

}

const dog = new Dog("レオ", 4);
dog.info();

// 定数humanAgeを定義し、定数dogに対してgetHumanAgeメソッドを呼び出した値を代入してください
const humanAge = dog.getHumanAge();

// 「人間年齢で〇〇歳です」と出力してください
console.log(`人間年齢で${humanAge}歳です`);


//----13.オーバーライド(1)----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

class Dog extends Animal {
  // infoメソッドを追加してください
  info(){
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
    
    const humanAge = this.getHumanAge();
    console.log(`人間年齢で${humanAge}歳です`);
  }

  getHumanAge() {
    return this.age * 7;
  }
}

const dog = new Dog("レオ", 4);
dog.info();


//----14.オーバーライド(2)----//
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  
  greet() {
    console.log("こんにちは");
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    console.log(`${this.age}歳です`);
  }
}

class Dog extends Animal {
  // constructorを追加してください
  constructor(name, age, breed){
    super(name, age);
    this.breed = breed;
  }
  
  info() {
    this.greet();
    console.log(`名前は${this.name}です`);
    // 「犬種は〇〇です」と出力してください
    console.log(`犬種は${this.breed}です`);
    
    console.log(`${this.age}歳です`);
    const humanAge = this.getHumanAge();
    console.log(`人間年齢で${humanAge}歳です`);
  }
  
  getHumanAge() {
    return this.age * 7;
  }
}

// 3つ目の引数に「"チワワ"」を渡してください
const dog = new Dog("レオ", 4, "チワワ");
dog.info();





////----Java script 学習レッスンⅤ----////
///----ファイルを分割しよう----///
//----2.ファイルの分割----//
// Dogクラスをインポートしてください
import Dog from "./dog";

const dog = new Dog("レオ", 4, "チワワ");
dog.info();



//----3.値のエクスポート----//


//----4.名前付きエクスポート----//
// 以下を書き換えて、定数dog1, dog2をインポートしてください
import {dog1, dog2} from "./dogData";

// 定数dog1とdog2を出力するように左からコピーして書き換えてください
console.log("---------");
dog1.info();
console.log("---------");
dog2.info();



//----5.相対パス----//
// "./dogData"(相対パス)を書き換えてください。
import { dog1, dog2 } from "./data/dogData";

console.log("---------");
dog1.info();
console.log("---------");
dog2.info();



//----6.パッケージ----//
//----7.パッケージ2----//





////----Java script 学習レッスンⅥ----////
///----配列の便利なメソッド----///
//----1.pushメソッド----//
const characters = ["にんじゃわんこ", "ベイビーわんこ", "ひつじ仙人"];

console.log(characters);

// pushメソッドを使って配列charactersに、文字列「とりずきん」を追加してください
characters.push("とりずきん");

// 配列charactersを出力してください
console.log(characters);


//----2.forEachメソッド----//
const characters = ["にんじゃわんこ", "ベイビーわんこ", "ひつじ仙人", "とりずきん"];

// forEachメソッドを使って、配列charactersの中身をすべて出力してください
characters.forEach((character) => {
  console.log(character);
});



//----3.findメソッド----//
const numbers = [1, 3, 5, 7, 9];

// findメソッドを使って配列numbersから3の倍数を見つけ、定数foundNumberに代入してください
const foundNumber = numbers.find((number) => {
  return number % 3 === 0;
});

// foundNumberを出力してください
console.log(foundNumber);


const characters = [
  {id: 1, name: "にんじゃわんこ", age: 6},
  {id: 2, name: "ベイビーわんこ", age: 2},
  {id: 3, name: "ひつじ仙人", age: 100},
  {id: 4, name: "とりずきん", age: 21}
];

// 定数charactersからidが3のオブジェクトを見つけ、定数foundCharacterに代入してください
const foundCharacter = characters.find((character)=>{
  return character.id === 3;
});

// foundCharacterを出力してください
console.log(foundCharacter);



//----4.filterメソッド----//
const numbers = [1, 2, 3, 4];

// filterメソッドを使ってnumbersから偶数を取り出し、定数evenNumbersに代入してください
const evenNumbers = numbers.filter((number)=>{
  return number % 2 ===0;
});

// evenNumbersを出力してください
console.log(evenNumbers);


const characters = [
  {id: 1, name:"にんじゃわんこ", age: 14},
  {id: 2, name:"ベイビーわんこ", age: 5},
  {id: 3, name:"ひつじ仙人", age: 100}
];

// charactersから20歳未満のキャラクターを取り出し、定数underTwentyに代入してください
const underTwenty = characters.filter((character)=>{
  return character.age < 20;
});

// underTwentyを出力してください
console.log(underTwenty);



//----5.mapメソッド----//
const numbers = [1, 2, 3, 4];

// 定数numbersにmapメソッドを使って配列を作り、定数doubledNumbersに代入してください
const doubledNumbers = numbers.map((number)=>{
  return number * 2;
});

// 定数doubledNumbersを出力してください
console.log(doubledNumbers);


const names = [
  {firstName: "Kate", lastName: "Jones"},
	{firstName: "John", lastName: "Smith"},
	{firstName: "Denis", lastName: "Williams"},
	{firstName: "David", lastName: "Black"}
];

// 定数namesにmapメソッドを使って新しい配列を作り、定数fullNamesに代入してください
const fullNames = names.map((name)=>{
  return name.firstName + name.lastName;
});

// 定数fullNamesを出力してください
console.log(fullNames);





////----Java Script学習レッスンⅦ----////
///----コールバック関数を学ぼう----///
//----1.コールバック関数を学ぼう----//
const printWanko = () => {
  console.log("にんじゃわんこ");
};

const printHitsuji = () => {
  console.log("ひつじ仙人");
};

const call = (callback) => {
  console.log("コールバック関数を呼び出します。");
  callback();
};

// 引数をprintHitsujiに書き換えて出力を確認しましょう
call(printHitsuji);


//----2.コールバック関数とは----//
const printWanko = () => {
  console.log("にんじゃわんこ");
};

// 関数callにcallbackという名前の引数を追加してください
const call = (callback) => {
  console.log("コールバック関数を呼び出します。");
  // 引数に渡したcallbackを呼び出してください
  callback();
};

// 関数printWankoを引数に渡して関数callを実行してください
call(printWanko);


//----3.コールバック関数を直接定義する----//
const printWanko = () => {
  console.log("にんじゃわんこ");
};

const call = (callback) => {
  console.log("コールバック関数を呼び出します。");
  callback();
};

call(printWanko);

// 引数で関数を定義して渡してください
call(() => {
  console.log("ひつじ仙人");
});



//----コールバック関数の引数----//
const call = (callback) => {
  callback("にんじゃわんこ", 14);
};

// 関数callの引数の中で2つの引数を取る関数を追加してください
call((name, age) => {
  console.log(`${name}は${age}歳です。`);
});
