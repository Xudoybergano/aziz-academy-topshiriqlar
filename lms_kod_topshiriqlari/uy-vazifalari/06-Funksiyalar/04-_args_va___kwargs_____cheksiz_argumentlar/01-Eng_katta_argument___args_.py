def eng_katta(*sonlar):
    return max(sonlar)

sonlar_list = list(map(int, input().split()))

print(eng_katta(*sonlar_list))