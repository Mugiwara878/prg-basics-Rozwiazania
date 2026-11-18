def longest_streak(dice):
    max_streak = 1          # najdłuższy znaleziony ciąg (zakładamy 1)
    current_streak = 1      # aktualny ciąg, w którym właśnie jesteśmy
    best_digit = dice[0]    # cyfra należąca do najdłuższego ciągu (na poczatku pierwsza)
    for i in range(1, len(dice)):     # zaczynamy od indeksu 1 (porównujemy z poprzednim)
        if dice[i] == dice[i-1]:      # czy aktualna cyfra = poprzednia?
            current_streak += 1       # tak -> ciąg się wydłuża
        else:
            current_streak = 1        # nie -> ciąg się urywa, zaczynamy liczyć od nowa
        if current_streak > max_streak:   # czy ten ciąg jest dłuższy niż dotychczasowy rekord?
            max_streak = current_streak   # tak -> zapamiętaj nową długość rekordu
            best_digit = dice[i]          # i zapamiętaj JAKĄ cyfrę ten rekord dotyczy
    return int(best_digit)