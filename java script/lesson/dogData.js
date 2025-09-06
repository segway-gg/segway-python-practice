// Dogクラスのインポートと定数dogを以下に張り付けてください
import Dog from "./dog";

const dog = new Dog("レオ", 4, "チワワ");

// 定数dogをエクスポートしてください
export default dog;

////////////////////////////////////////////////

import Dog from "./dog";

// 定数dog1, dog2を確認してください
const dog1 = new Dog("レオ", 4, "チワワ");
const dog2 = new Dog("ベン", 2, "プードル");

// 以下を書き換えて、定数dog1, dog2をエクスポートしてください
export {dog1, dog2};



////////////////////////////////////////////////
// "./dog"(相対パス)を書き換えてください。
import Dog from "../class/dog";

const dog1 = new Dog("レオ", 4, "チワワ");
const dog2 = new Dog("ベン", 2, "プードル");

export { dog1, dog2 };


/////////////////////////////////////////////////
//----7.パッケージ2----//
// readline-syncをインポートしてください
import readlineSync from "readline-sync"; 

import Dog from "../class/dog";

const dog1 = new Dog("レオ", 4, "チワワ");

// readlineSync.questionを使って書き換えてください
const name = readlineSync.question("名前を入力してください: ");

// readlineSync.questionIntを使って書き換えてください
const age = readlineSync.questionInt("年齢を入力してください: ");

// readlineSync.questionを使って書き換えてください
const breed = readlineSync.question("犬種を入力してください: ");

const dog2 = new Dog(name, age, breed);

export { dog1, dog2 };