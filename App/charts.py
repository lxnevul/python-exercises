import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')    #Revisar, parece que ya viene por defecto este valor al ser un pie chart
    plt.show()

if __name__ == '__main__':
    labels = ['laptop', 'mouse', 'router']
    values = [800, 60, 150]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)