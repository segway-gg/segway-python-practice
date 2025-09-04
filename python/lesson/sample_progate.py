print("Hello, python!")

##----入門----##

# 数値の 7 を出力してください
print(7)

# 9 に 3 足した値を出力してください
print(9 + 3)

# 「 9 + 3 」を文字列として出力してください
print('9 + 3')

# 9 を 2 で割った値を出力してください
print(9/2)

# 7 に 5 を掛けた値を出力してください
print(7*5)

# 5 を 2 で割った時の余りを出力してください
print(5%2)

# 変数 name に文字列「 にんじゃわんこ 」を代入してください
name ='にんじゃわんこ'

# 変数 name の値を出力してください
print(name)

# 変数 number に数値の 7 を代入してください
number = 7

# 変数 number の値を出力してください
print(number)

apple_price = 200
apple_count = 8

# apple_price と apple_count を掛けた結果を、変数 total_price に代入してください
total_price = apple_price * apple_count

# total_price の値を出力してください
print(total_price)

money = 2000
print(money)

# 変数 money に 5000 を足して、変数 money を上書きしてください
money += 5000

# 変数 money の値を出力してください
print(money)

# my_name という変数に「 にんじゃわんこ 」という文字列を代入してください
my_name = 'にんじゃわんこ'

# my_name を用いて、「私はにんじゃわんこです」となるように変数と文字列を連結して出力してください
print('私は' + my_name + 'です')

age = 24
# age を用いて「私は24歳です」と出力してください
print('私は' + str(age) + '歳です')

count = '5'
# count に 1 を足した値を出力してください
print(int(count) + 1)
##----入門----##



##----条件分岐----##
x = 7 * 10
y = 5 * 6

# x が 70 と等しい場合に「 xは70です 」と出力してください
if x == 70:
    print("xは70です")


# y が 40 と等しくない場合に「 yは40ではありません 」と出力してください
if y != 40:
    print("yは40ではありません")

x = 10
# x が 30 より大きい場合に「 xは30より大きいです 」と出力してください
if x > 30:
    print("xは30より大きいです")


money = 500
apple_price = 200
# money の値が apple_price の値以上の時、「 りんごを買うことができます 」と出力してください
if money >= apple_price:
    print("りんごを買うことができます")

money = 100
apple_price = 200

if money >= apple_price:
    print('りんごを買うことができます')
# if 文の条件に当てはまらない場合に「 お金が足りません 」と出力してください
else:
    print('お金が足りません')

money = 100
apple_price = 100

if money > apple_price:
    print('りんごを買うことができます')
# 変数の値が等しい場合に「 りんごを買うことができますが所持金が0になります 」と出力してください
elif money == apple_price:
    print("りんごを買うことができますが所持金が0になります")

else:
    print('お金が足りません')

x = 20
# 変数 x が 10 以上 30 以下の場合に「 xは10以上30以下です 」と出力してください
if 10 <= x <= 30:
    print('xは10以上30以下です')


y = 60
# 変数 y が 10 未満または 30 より大きい場合に「 yは10未満または30より大きいです 」と出力してください
if y < 10 or y >30:
    print('yは10未満または30より大きいです')


z = 55
# 変数 z が 77 ではない場合に「 zは77ではありません 」と出力してください
if not z ==77:
    print('zは77ではありません')



##----15.代金を計算しよう----##
# apple_price という変数に数値 200 を代入してください
apple_price = 200

# count という変数に数値 5 を代入してください
count = 5

# total_price という変数に、 apple_price と count を掛けたものを代入してください
total_price = apple_price * count

# 「 購入するりんごの個数は○○個です 」となるように出力してください
print('購入するりんごの個数は' + str(count) + '個です')

# 「 支払い金額は○○円です 」となるように出力してください
print('支払い金額は' + str(total_price)+ '円です')



##----16.入力を受け取ろう----##
apple_price = 200

# input を用いて入力を受け取り、変数 input_count に代入してください
input_count = input('購入するりんごの個数を入力してください：')

# input_count を数値として代入してください
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')



##----17.条件分岐をしよう----##
apple_price = 200
# 変数 money に数値 1000 を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# money と total_price の比較結果によって条件を分岐してください
if total_price < money:
    print('りんごを' + str(count) + '個買いました')
    print('残金は' + str(money - total_price) +'円です')
elif total_price == money:
    print('りんごを' + str(count) + '個買いました')
    print('財布が空になりました')
else:
    print('お金が足りません')
    print('りんごを買えませんでした')

###----条件分岐----##





####----Python学習レッスンⅡ----####
###----複数のデータを扱おう----###
##----2.リスト----##
# 変数 fruits に、複数の文字列を要素に持つリストを代入してください
fruits = ['apple', 'banana', 'orange']

# インデックス番号が 0 の要素を出力してください
print(fruits[0])

# インデックス番号が 2 の要素を文字列と連結して出力してください
print('好きな果物は' + fruits[2] + 'です')



##----3.リストの要素の更新・追加----##
fruits = ['apple', 'banana', 'orange']

# リストの末尾に文字列「 grape 」を追加してください
fruits.append('grape')

# 変数 fruits に代入したリストを出力してください
print(fruits)

# インデックス番号が 0 の要素を文字列「 cherry 」に更新してください
fruits[0] = 'cherry'

# インデックス番号が 0 の要素を出力してください
print(fruits[0])



##----4.リストの要素を全て取得しよう----##
fruits = ['apple', 'banana', 'orange']

# for 文を用いてリストの要素を1つずつ取り出し、「 好きな果物は◯◯です 」と出力してください
for fruit in fruits:
    print('好きな果物は' + fruit + 'です')



##----5.辞書----##
# 変数 fruits に辞書を代入してください
fruits = {'apple':'りんご', 'banana':'バナナ'}

# 辞書 fruits のキー「 banana 」に対応する値を出力してください
print(fruits['banana'])

# 辞書 fruits を用いて、「 appleは◯◯という意味です 」となるように出力してください
print('appleは'+ fruits['apple'] + 'という意味です')



##----6.辞書の要素の更新・追加----##
fruits = {'apple': 100, 'banana': 200, 'orange': 400}

# キー「 banana 」の値を数値 300 に更新してください
fruits['banana'] = 300

# キーが「 grape 」、値が数値の 500 の要素を辞書 fruits に追加してください
fruits['grape'] = 500

# fruits の値を出力してください
print(fruits)



##----7.for文(2)----##
fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# for 文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「 ◯◯は△△という意味です 」と出力させてください
for fruit_key in fruits:
    print(fruit_key + 'は' + fruits[fruit_key] + 'という意味です')



##----8.while文----##
x = 10

# while 文を用いて、「変数 x が 0 より大きい」間、繰り返される繰り返し処理を作ってください
while x > 0:
    # 変数 x を出力してください
    print(str(x))
    # 変数 x から 1 引いてください
    x -= 1



##----9.break文----##
numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # 変数 number が 777 のとき「 777が見つかったので処理を終了します 」と出力した後、処理を終了させてください
    if number == 777:
        print('777が見つかったので処理を終了します')
        break



##----10.continue文----##
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # 変数 number の値が 3 の倍数のとき、繰り返し処理をスキップしてください
    if number % 3 == 0:
        continue
    
    print(number)



##----11.商品を用意しよう----##
# 文字列のキーと数値の値を持つ辞書を作って、変数 items に代入してください
items = {'apple':100, 'banana':200, 'orange':400}

# for 文を用いて、辞書 items のキーを1つずつ取り出していく繰り返し処理を作成してください
for item_name in items:
    # 「 --------------------------------------------- 」を出力してください
    print('---------------------------------------------')
    # 「 ◯◯は1個△△円です 」となるように出力してください
    print(item_name + 'は1個' + str(items[item_name]) + '円です')



##----12.商品を選んでもらおう----##
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    # input を用いて入力を受け取り、変数 input_count に代入してください
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    # キーと変数 input_count を用いて「 購入する◯◯の個数は△△個です 」となるように出力してください
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    
    # input_count を数値として変数 count に代入してください
    count = int(input_count)
    # 変数 total_price に果物1個の値段と変数 count を掛けた値を代入してください
    total_price = items[item_name] * count
    # 変数 total_price と型変換を用いて、「 支払い金額は◯◯円です 」となるように出力してください
    print('支払い金額は' + str(total_price) + '円です')



##----13.条件分岐をしよう----##
# 変数 money に数値 1000 を代入してください
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    # 変数 money を用いて「 財布には◯◯円入っています 」のように出力してください
    print('財布には' + str(money) + '円入っています')
    
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    # money と total_price の比較結果によって条件を分岐してください
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')



##----14.残金を計算しよう----##
money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')
    
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        # if 文を用いて、 money の値が 0 のときの条件を分岐してください
        if money == 0:
            print('財布が空になりました')
            break
        
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
# 変数 money と型変換を用いて、「 残金は◯◯円です 」となるように出力してください
print('残金は' + str(money) + '円です')



####----Python学習レッスンⅡ終了----####





####----Python学習レッスンⅢ----####
###----関数----###
##----2.関数----##
# 関数 print_hand を定義してください
def print_hand():
    print('グーを出しました')
# 関数 print_hand を呼び出してください
print_hand()


##----3.引数----##
# 引数を受け取れるようにしてください
def print_hand(hand):
    # 「 ◯◯を出しました 」と出力されるように書き換えてください
    print(hand + 'を出しました')

# 引数に文字列「 グー 」を入れてください
print_hand('グー')

# 引数を文字列「 パー 」として関数 print_hand を呼び出してください
print_hand('パー')



##----4.複数の引数----##
# 名前を第2引数で受け取れるようにしてください
def print_hand(hand, name):
    # 「 ◯◯は□□を出しました 」と出力されるように書き換えてください
    print(name + 'は' + hand + 'を出しました')

# 第2引数に文字列「 にんじゃわんこ 」を入れてください
print_hand('グー', 'にんじゃわんこ')

# 第2引数に文字列「 コンピューター 」を入れてください
print_hand('パー', 'コンピューター')



##----5.引数の初期値----##
# 仮引数 name の初期値を設定してください
def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

# 引数に文字列「 グー 」のみを入れてください
print_hand('グー')



##----6.名前を受け取ろう----##
def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

# input を用いて入力を受け取り、変数 player_name に代入してください
player_name = input('名前を入力してください：')

# 変数 player_name の値によって関数 print_hand の呼び出し方を変更してください
if player_name == '':
    print_hand('グー')
else:
    print_hand('グー', player_name)



##----7.出す手を選べるようにしよう----##
def print_hand(hand, name='ゲスト'):
    # 変数 hands に、複数の文字列を要素に持つリストを代入してください
    hands = ['グー', 'チョキ', 'パー']
    
    # リスト hands を用いて、選択した手が出力されるように書き換えましょう
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# 「 何を出しますか？（0: グー, 1: チョキ, 2: パー） 」と出力してください
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')

# input を用いて入力を受け取り、数値に型変換してから変数 player_hand に代入してください
player_hand = int(input('数字で入力してください：'))

if player_name == '':
    # 第1引数を変数 player_hand に書き換えてください
    print_hand(player_hand)
else:
    # 第1引数を変数 player_hand に書き換えてください
    print_hand(player_hand, player_name)



##----8.戻り値----##
# 関数 validate を定義してください
def validate(hand):
    # hand の値によって条件分岐してください
    if 0 > hand or hand > 2:
        return False
    else:
        return True
        
def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数 validate の戻り値が True の場合、以下の if~else 文が実行されるようにしてください
if validate(player_hand) == True:
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# 関数 validate の戻り値が False の場合「 正しい数値を入力してください 」と出力してください
else :
    print('正しい数値を入力してください')



##----9.returnの性質----##
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    # else を消してインデントを直してください
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
else:
    print('正しい数値を入力してください')



##----10.じゃんけんをしよう----##
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    # 変数 computer_hand に数値 1 を代入してください
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    # 第1引数を computer_hand 、第2引数を文字列「 コンピューター 」として関数 print_hand を呼び出してください
    print_hand(computer_hand, 'コンピューター')

else:
    print('正しい数値を入力してください')



##----11.勝敗を判定しよう----##
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# 関数 judge を定義してください
def judge(player, computer):
    # player と computer の比較結果によって条件を分岐してください
    if player == computer:
        return '引き分け'
    elif player == 0 and computer == 1:
        return  '勝ち'
    elif player == 1 and computer == 2:
        return  '勝ち'
    elif player == 2 and computer == 0:
        return  '勝ち'
    else:
        return '負け'
    

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    print_hand(computer_hand, 'コンピューター')
    
    # 変数 result に関数 judge の戻り値を代入してください
    result = judge(player_hand, computer_hand)
    # 変数 result を出力してください
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')



##----12.モジュールを使おう----##
# 3つの関数のコードを utils.py に移してください（こちらのコードは消してください）

# utils.py をモジュールとして読み込んでください
import utils # type: ignore

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# utils モジュール内の関数 validate を呼び出してください
if utils.validate(player_hand):
    computer_hand = 1

    if player_name == '':
        # utils モジュール内の関数 print_hand を呼び出してください
        utils.print_hand(player_hand)
    else:
        # utils モジュール内の関数 print_hand を呼び出してください
        utils.print_hand(player_hand, player_name)

    # utils モジュール内の関数 print_hand を呼び出してください
    utils.print_hand(computer_hand, 'コンピュータ')
    
    # utils モジュール内の関数 judge を呼び出してください
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')



##----13.ライブラリを使おう----##
import utils # type: ignore
# random モジュールを読み込んでください
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if utils.validate(player_hand):
    # randint を用いて 0 から 2 までの数値を取得し、変数 computer_hand に代入してください
    computer_hand = random.randint(0, 2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'コンピューター')
    
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')





####----Python学習レッスンⅣ----####
###----クラスとインスタンス----###
##----2.クラスの定義----####
# MenuItem クラスを定義してください
class MenuItem:
    pass


##----3.インスタンスの生成----##
class MenuItem:
    pass
# MenuItem クラスのインスタンスを生成してください
menu_item1 = MenuItem()



##----4.インスタンス変数----##
class MenuItem:
    pass


menu_item1 = MenuItem()

menu_item1.name = 'サンドイッチ'
print(menu_item1.name)

# menu_item1 の price に 500 を代入してください
menu_item1.price = 500

# menu_item1 の price を出力してください
print(menu_item1.price)



##----5.複数のインスタンス----##
class MenuItem:
    pass


menu_item1 = MenuItem()

menu_item1.name = 'サンドイッチ'
print(menu_item1.name)

menu_item1.price = 500
print(menu_item1.price)

# MenuItem クラスのインスタンスを生成してください
menu_item2 = MenuItem()

# menu_item2 の name に「 チョコケーキ 」を代入してください
menu_item2.name = 'チョコケーキ'

# menu_item2 の name を出力してください
print(menu_item2.name)

# menu_item2 の price に 400 を代入してください
menu_item2.price = 400

# menu_item2 の price を出力してください
print(menu_item2.price)



##----6.クラスとメソッド----##
class MenuItem:
    # info メソッドを定義してください
    def info(self):
        print('メニューの名前と値段が表示されます')


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1 に対して info メソッドを呼び出してください
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2 に対して info メソッドを呼び出してください
menu_item2.info()



##----7.インスタンスメソッド----##
class MenuItem:
    def info(self):
        # 「 ○○: ¥□□ 」となるように出力してください
        print(self.name + ': ¥' + str(self.price))


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

menu_item2.info()



##----8.インスタンスメソッドの活用(戻り値)----##
class MenuItem:
    def info(self):
        # print() の中身を戻り値として返してください
        return self.name + ': ¥' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1.info() の値を出力してください
print(menu_item1.info())

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2.info() の値を出力してください
print(menu_item2.info())



##----9.インスタンスメソッドの活用(引数)----##
class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_price メソッドを定義してください
    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

# get_total_price メソッドを呼び出してください
result = menu_item1.get_total_price(4)

# 「 合計は〇〇円です 」となるように出力してください
print('合計は' + str(result) + '円です')



##----10.特殊なインスタンスメソッド(__init__)----##
class MenuItem:
    # __init__ メソッドを定義してください
    def __init__(self):
        print('MenuItemクラスのインスタンスが生成されました！')

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

result = menu_item1.get_total_price(4)

print('合計は' + str(result) + '円です')



##----11.__init__のメソッド----##
class MenuItem:
    def __init__(self):
        # self.name に「 サンドイッチ 」を代入してください
        self.name = 'サンドイッチ'
        
        # self.price に 500 を代入してください
        self.price = 500

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
# 以下の2行は削除してください

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')



##----12.__init__のメソッドに引数を渡そう----##
class MenuItem:
    # 引数 name と price を受け取るようにしてください
    def __init__(self, name, price):
        # 「 サンドイッチ 」の代わりに引数 name の値を代入してください
        self.name = name
        
        # 500 の代わりに引数 price の値を代入してください
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# 引数を「 サンドイッチ 」と 500 としてください
menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')



##----13.ファイルの分割----##
# この行より上のコードを「 menu_item.py 」に移動してください

# menu_item.py から MenuItem クラスを読み込んでください
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')



##----14.メニュー一覧の作成（1）----##
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

# 指定されたリストを変数 menu_items に代入してください
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# for 文を作成してください
for item in menu_items:
    print(item.info())



##----15.メニュー一覧の作成（2）----##
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# 変数 index を定義し、数値の 0 を代入してください
index = 0

for item in menu_items:
    # 「 0. サンドイッチ: ¥500 」となるように出力してください
    print(str(index) + '.' + item.info())
    
    # 変数 index に 1 を加えてください
    index += 1



##----16.入力を受け取る----##
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for item in menu_items:
    print(str(index) + '. ' + item.info())
    index += 1

print('--------------------')

# コンソールから入力を受け取り、変数 order に代入してください
order = int(input('メニューの番号を入力してください: '))

# 選択されたメニューを変数 selected_menu に代入してください
selected_menu = menu_items[order]

# 「 選択されたメニュー: 〇〇 」と出力してください
print('選択されたメニュー: ' + selected_menu.name)





####----Python学習レッスンⅤ----####
###----クラスの継承----###
##----2.継承とは----##
#ほかのFileを作成したので参照してください food.py drink.py



##----3.継承のしくみ----##
# Food クラスと Drink クラスをそれぞれ読み込んでください
from food import Food
from drink import Drink


# Food クラスのインスタンスを生成して変数 food1 に代入してください
food1 = Food('サンドイッチ', 500)

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())

# Drink クラスのインスタンスを生成して変数 drink1 に代入してください
drink1 = Drink('コーヒー', 300)

# drink1 に対して info メソッドを呼び出して戻り値を出力してください
print(drink1.info())



##----4.インスタンスメソッドの追加----##
from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500)

# food1 の calorie に 330 を代入してください
food1.calorie = 330

# food1 に対して calorie_info メソッドを呼び出してください
food1.calorie_info()



##----5.オーバーライド----##
from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500)
food1.calorie = 330

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())



###----6.infoメソッドの改良(2)----##
from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500)
food1.calorie = 330
print(food1.info())

# Drink クラスのインスタンスを生成して変数 drink1 に代入してください
drink1 = Drink('コーヒー', 300)

# drink1 の amount に 180 を代入してください
drink1.amount = 180

# drink1 に対して info メソッドを呼び出して戻り値を出力してください
print(drink1.info())



##----7.__init__メソッドのオーバーライド----##
from food import Food
from drink import Drink

# Food() に引数を追加してください
food1 = Food('サンドイッチ', 500, 330)

# 以下の1行は削除してください


print(food1.info())

drink1 = Drink('コーヒー', 300)
drink1.amount = 180
print(drink1.info())



##----9.オーバーライトの復習----##
from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500, 330)
print(food1.info())

# Drink() に引数を追加してください
drink1 = Drink('コーヒー', 300, 180)

# 以下の1行は削除してください

print(drink1.info())
