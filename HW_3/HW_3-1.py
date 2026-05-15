from collections import deque


# =========================
# HW3-1：智能派單 Smart Enqueue
# =========================

# 初始黃金
player_gold = 180

# 每種兵種的價格
cost_table = {
    "劍士": 50,
    "弓手": 80,
    "騎士": 80,
    "法師": 120
}

# 測試訂單
# 若老師 Colab 有提供 orders，請把這裡換成老師的 orders
orders = [
    {"unit": "劍士"},
    {"unit": "弓手"},
    {"unit": "騎士"},
    {},
    {"unit": "法師"},
    {"unit": "劍士"},
    {"unit": "弓手"},
    {},
]

# A、B 兩條產線
queue_a = deque()
queue_b = deque()

# 每條產線最多只能排 2 個
MAX_QUEUE_SIZE = 2


def dequeue_factory(factory_name, queue):
    """兵營出列，並處理 Underflow 防呆。"""
    if len(queue) > 0:
        unit = queue.popleft()
        print(f"{factory_name} 廠生產完成：{unit} 出列！")
    else:
        print(f"{factory_name} 廠沒東西可做（Underflow 防護成功）")


def smart_enqueue(unit, gold):
    """根據金錢、Overflow、負載平衡規則，把兵種放入 A 或 B 產線。"""

    cost = cost_table[unit]

    # 資源檢核
    if gold < cost:
        print(f"黃金不足，無法生產 {unit}")
        return gold

    # Overflow 防禦
    if len(queue_a) >= MAX_QUEUE_SIZE and len(queue_b) >= MAX_QUEUE_SIZE:
        print(f"產線全滿！{unit} 訂單拒絕")
        return gold

    # 負載平衡：排隊人數較少者優先，一樣長則放 A
    if len(queue_a) <= len(queue_b):
        queue_a.append(unit)
        gold -= cost
        print(f"{unit} 分派至 A 廠（剩餘黃金：{gold}）")
    else:
        queue_b.append(unit)
        gold -= cost
        print(f"{unit} 分派至 B 廠（剩餘黃金：{gold}）")

    return gold


print("========== HW3-1：智能派單 ==========")

for round_idx, order in enumerate(orders):
    print(f"\n--- 第 {round_idx} 回合 ---")

    # 偶數回合自動觸發雙廠 Dequeue
    if round_idx % 2 == 0:
        if order == {}:
            print("玩家本回合無動作，單純推進時間")

        dequeue_factory("A", queue_a)
        dequeue_factory("B", queue_b)

    # 空單不做生產
    if order == {}:
        print(f"A：{list(queue_a)} | B：{list(queue_b)}")
        continue

    # 讀取訂單兵種
    unit = order["unit"]

    # 執行智能派單
    player_gold = smart_enqueue(unit, player_gold)

    # 顯示目前產線狀態
    print(f"A：{list(queue_a)} | B：{list(queue_b)}")