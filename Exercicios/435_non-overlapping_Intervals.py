class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        # Ordena os intervalos com base no ponto final em ordem crescente
        intervals.sort(key=lambda x: x[1])

        count = 1
        end = intervals[0][1]

        # Percorre os intervalos a partir do segundo
        for i in range(1, len(intervals)):
            # Se o intervalo atual não se sobrepõe ao anterior,
            # incrementa o contador e atualiza o ponto final
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        # Retorna o número de intervalos a serem removidos
        return len(intervals) - count
