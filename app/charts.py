import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./img/{name} grafico de Barras.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.savefig('pie.png')
    plt.close()

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [1000, 200, 88]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)