try:
    with open("C:/개발자 학습용 게임/stage 6~10/numbers.txt", "r", encoding="utf-8") as f:
        nums = [int(x) for x in f.read().split()]

    if not nums:
        print("데이터가 없습니다.")
    else:
        print("SUM:", sum(nums))
        print("AVG:", sum(nums)/len(nums))

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")