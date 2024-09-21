import time as t

def ft_progress(elems):
    # tempo inicial
    inicio = t.time()

    for i in elems:
        # porcentagem
        percen = ((i+1)/len(elems)) * 100

        # barra de progresso
        total = (percen / 10)
        progresso = ("=" * int(total)) + ">" + (" " * (10-int(total)))

        # tempo total
        fim = t.time()
        tempo_total = fim - inicio

        # ETA
        eta = ((tempo_total / percen) * 100) - tempo_total
        #eta = ((tempo_total / percen) * 100)

        # imprimindo porcentagem
        print(f"ETA: {eta:.2f}s [{percen:.0f}%][{progresso}] {i+1}/{len(elems)} | elapsed time {tempo_total:.2f}s", end="\r")
        yield i

a_list = range(1000)
ret = 0

# execução
for elem in ft_progress(a_list):
    ret += (elem + 3) % 5
    t.sleep(0.01)

print()
print(ret)

