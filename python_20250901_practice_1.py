####----演習1----####
name = 'Shinei Miyasaka'
age = 26
print('私は' + name + 'です。' + str(age) + '歳です。')

price = 120
num = 3
print(price * num)



####----演習2----####
fruits = ['いちご', 'みかん', 'ぶどう']
fruits.append('なし')
print(fruits) 


####----演習3----####
user_name = input('あなたの名前を入力してください：')
print('こんにちは、' + user_name + 'さん！')

user_num1 = input('1つ目の数字を入力してください：')
user_num2 = input('2つ目の数字を入力してください：')
print(int(user_num1) + int(user_num2))


####----演習4----####
friends = ["Taro", "Hanako", "Ken"]
for friend in friends:
    print(friend + 'さん、こんにちは！')