####----演習1----####
# カート内の商品の有無に合わせてメッセージを返す処理を作成してください
def get_cart_message(cart_items):
    if len(cart_items) == 0:
        return 'カートに商品がありません。お買い物をお楽しみください。'
    else:
        return '購入手続きを進めるか、引き続きお買い物をお楽しみください。'

# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
# 関数の呼び出し
message = get_cart_message(cart_items)
print('入力1：カートに商品がある場合')
print(message)

print('-----------------------------')

# 利用するデータ
cart_items = []
# 関数の呼び出し
message = get_cart_message(cart_items)
print('入力2：カートに商品がない場合')
print(message)





####----演習2----####
# 購入金額に対する付与ポイントを返す処理を作成してください
def calculate_points(total_price, user):
    if user['status'] == 'premium':
        points =  total_price * (0.01 + 0.01)
        return round(points) ## 小数点以下を四捨五入して整数にする
    else:
        points =  total_price * 0.01
        return round(points)

# ここから下は触らないでください
# 利用するデータ
total_price = 10000

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがbasicの場合')
print(points)

print('-----------------------------')

# 利用するデータ
user = {'user_id': 2, 'status': 'premium'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがpremiumの場合')
print(points)





####----演習3----####
# カート内の商品の税込合計金額を返す処理を作成してください
#関数作成
def calculate_total_with_tax(cart_items, tax_rate):
    #合計金額の初期値の設定
    total_price = 0
    #税抜きの合計金額の合計を出す
    for cart_item in cart_items:
        total_price = total_price + cart_item['price']
        print(total_price)

    #合計金額に対して税の計算を行う(10%)
    total_tax =  total_price * tax_rate
    #税込み合計金額を計算する
    return round(total_price + total_tax)

# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
tax_rate = 0.1
# 関数の呼び出し
total_with_tax = calculate_total_with_tax(cart_items, tax_rate)
print(total_with_tax)




####----演習4----####
# 対象ユーザーの注文履歴を返す処理を作成してください            
                    
def get_order_history(user, orders):            
    user_orders = []            
    # 繰り返し処理で注文履歴リストを1件ずつ取得する            
    for order in orders:            
        # 対象のユーザーの注文履歴かどうかを判別する            
        if order['user_id'] == user['user_id']:          
            # 対象ユーザーの注文履歴の場合、対象ユーザーの注文履歴リストに注文履歴を追加する            
            user_orders.append(order)            
        # 対象ユーザーの注文履歴リストを返す            
    return user_orders
        

# ここから下は触らないでください
# 利用するデータ
orders = [
    {
        'order_id': 1,
        'user_id': 1,
        'items': [
            {'name': 'キャップ', 'type': 'cap', 'price': 8000},
            {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000}
        ]
    },
    {
        'order_id': 2,
        'user_id': 2,
        'items': [
            {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
        ]
    },
    {
        'order_id': 3,
        'user_id': 1,
        'items': [
            {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
        ]
    },
    {
        'order_id': 4,
        'user_id': 3,
        'items': [
            {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
            {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000}          
        ]
    }
]

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
user_orders = get_order_history(user, orders)
for order in user_orders:
    print(order)





####----演習5----####
# 各商品と各色の組み合わせを全て出力する処理を作成してください
#商品リストと色の種類のリストを受け取る関数を作る
def display_product_and_color(items, colors):
    #繰り返し処理で商品リストを1件ずつ取得する
    for item in items:
        #繰り返し処理で色の種類リストを1件ずつ取得する
        for color in colors:
            #商品名と合わせて出力する
            print(item['name'] + ':' + color)
    
    

# ここから下は触らないでください
# 利用するデータ
items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
colors = ['Red', 'Blue', 'Black']
# 関数の呼び出し
display_product_and_color(items, colors)




####----演習6----####
# カート内の合計金額を返す処理を作成してください
#カート内の商品リストを引数に持つcalculate_total_price関数を作成する
def calculate_total_price(cart_items):
    total_price = 0
    #商品リストの各商品を取得するために商品の分だけ繰り返す
    for cart_item in cart_items:
        #種類に応じた条件分岐をする
        #種類がfoodの場合は10%引き
        if cart_item['type'] == 'food':
            cart_item['price'] *= 0.9
            total_price += round(cart_item['price'])
        #種類がclothesの場合は1000円引き
        elif cart_item['type'] == 'clothes':
            cart_item['price'] -= 1000
            total_price += cart_item['price']
        else:
            total_price += cart_item['price']
    return total_price

# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000},
    {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
    {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
    {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000},
    {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
]
# 関数の呼び出し
total_price = calculate_total_price(cart_items)
print(total_price)




