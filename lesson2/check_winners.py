def check_winners(scores, student_score):
    sub_scores = sorted(scores)[-3:]
    if student_score in sub_scores:
        print("Вы в тройке победителей")
    else:
        print("Вы не попали в тройку победителей")


def main():
    scores = [5, 4, 10, 9, 6, 7]
    student_score = 7
    check_winners(scores, student_score)


main()
