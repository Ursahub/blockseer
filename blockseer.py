import argparse
from blockseer.predictor import predict_inclusion_probability

def main():
    parser = argparse.ArgumentParser(description="🔮 Blockseer — предсказание подтверждения транзакций")
    parser.add_argument("--fee-rate", type=int, required=True, help="Комиссия в сат/байт")
    parser.add_argument("--blocks", type=int, default=3, help="Число будущих блоков для анализа (по умолчанию 3)")

    args = parser.parse_args()
    fee_rate = args.fee_rate
    blocks = args.blocks

    try:
        probability, position, capacity = predict_inclusion_probability(fee_rate, blocks)
        print(f"\n📬 Анализ для комиссии {fee_rate} сат/байт:")
        print(f"🔸 Вероятность включения в ближайшие {blocks} блок(а/ов): {probability}%")
        if position:
            print(f"🔸 Позиция в мемпуле (примерно): {position} vbytes")
            print(f"🔸 Прогнозируемое время ожидания: ~{(blocks * 10)}-минутный интервал")
        else:
            print("⚠️ Комиссия слишком низкая — транзакция может быть проигнорирована ближайшее время.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
