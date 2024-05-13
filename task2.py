import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графа
G = nx.Graph()

# Додавання вузлів станцій для першої гілки
first_branch_stations = ['Lisova', 'Chernihivska', 'Darnytsia', 'Livoberezhna', 'Hidropark', 'Dnipro', 'Arsenalna', 'Khreschatyk', 'Teatralna', 'Universitet', 'Vokzalna', 'Politekhnika', 'Shuliavska', 'Berestiyska', 'Sviatishin', 'Zhitimyrska', 'Akademmistechko']

G.add_nodes_from(first_branch_stations)

# Додавання ребер між станціями
connections = [
    ('Lisova', 'Chernihivska', {'weight':11}), 
    ('Chernihivska', 'Darnytsia', {'weight':11}), 
    ('Darnytsia', 'Livoberezhna', {'weight':10}), 
    ('Livoberezhna', 'Hidropark', {'weight':11}), 
    ('Hidropark', 'Dnipro', {'weight':11}), 
    ('Dnipro', 'Arsenalna', {'weight':11}), 
    ('Arsenalna', 'Khreschatyk', {'weight':11}), 
    ('Khreschatyk', 'Teatralna', {'weight':9}), 
    ('Teatralna', 'Universitet', {'weight':9}),
    ('Universitet','Vokzalna', {'weight':10}),
    ('Vokzalna','Politekhnika', {'weight':11}), 
    ('Politekhnika', 'Shuliavska', {'weight':10}), 
    ('Shuliavska', 'Berestiyska', {'weight':9}), 
    ('Berestiyska', 'Sviatishin', {'weight':11}), 
    ('Sviatishin', 'Zhitimyrska', {'weight':11}), 
    ('Zhitimyrska', 'Akademmistechko', {'weight':5})
    ]

# Додавання станцій другої гілки
second_branch_stations = ['Syrets', 'Dorohozhychi', 'Lukianivska', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi']

# Додаємо нові станції до графа
G.add_nodes_from(second_branch_stations)

# Додавання ребер між станціями другої гілки
second_branch_connections = [
    ('Syrets', 'Dorohozhychi', {'weight':7}), 
    ('Dorohozhychi', 'Lukianivska', {'weight':14}), 
    ('Lukianivska', 'Zoloti Vorota', {'weight':15}), 
    ('Zoloti Vorota', 'Palats Sportu', {'weight':10}), 
    ('Palats Sportu', 'Klovska', {'weight':11}), 
    ('Klovska', 'Pecherska', {'weight':11}), 
    ('Pecherska', 'Druzhby Narodiv', {'weight':11}), 
    ('Druzhby Narodiv', 'Vydubychi', {'weight':13})
    ]

# Додавання станцій для синьої гілки
blue_branch_stations = ['Minska', 'Obolon', 'Petrovka', 'Tarasa Shevchenko', 'Kontraktova Ploshcha', 'Poshtova Ploshcha', 'Maidan Nezalezhnosti', 'Ploshcha Lva Tolstogo', 'Olimpiiska', 'Palats Ukraina', 'Lybidska', 'Demiivska', 'Holosiivska', 'Vasylkivska', 'Vystavkovyi Tsentr', 'Ipodrom', 'Teremky']

# Додавання станцій до графа
G.add_nodes_from(blue_branch_stations)

# Додавання ребер між станціями синьої гілки
blue_branch_connections = [
    ('Minska', 'Obolon', {'weight':14}), 
    ('Obolon', 'Petrovka', {'weight':12}), 
    ('Petrovka', 'Tarasa Shevchenko', {'weight':11}), 
    ('Tarasa Shevchenko','Kontraktova Ploshcha', {'weight':14}), 
    ('Kontraktova Ploshcha','Poshtova Ploshcha', {'weight':10}),
    ('Poshtova Ploshcha','Maidan Nezalezhnosti', {'weight':11}), 
    ('Maidan Nezalezhnosti','Ploshcha Lva Tolstogo', {'weight':10}), 
    ('Ploshcha Lva Tolstogo','Olimpiiska', {'weight':13}),
    ('Olimpiiska','Palats Ukraina', {'weight':11}), 
    ('Palats Ukraina','Lybidska', {'weight':10}),
    ('Lybidska','Demiivska', {'weight':11}), 
    ('Demiivska','Holosiivska', {'weight':9}),
    ('Holosiivska','Vasylkivska', {'weight':15}),
    ('Vasylkivska','Vystavkovyi Tsentr', {'weight':16}),
    ('Vystavkovyi Tsentr','Ipodrom', {'weight':10}),
    ('Ipodrom', 'Teremky', {'weight':13})
    ]
G.add_edges_from(blue_branch_connections)


# Додавання ребер
G.add_edges_from(connections)
G.add_edges_from(second_branch_connections)

# Вузли, які перетинаються
intersection_nodes = ['Teatralna', 'Zoloti Vorota', 'Maidan Nezalezhnosti', 'Khreschatyk', 'Palats Sportu', 'Ploshcha Lva Tolstogo']

# Додавання ребер для точок перетину
intersection_edges = [('Teatralna', 'Zoloti Vorota'), ('Khreschatyk', 'Maidan Nezalezhnosti'), ('Palats Sportu', 'Ploshcha Lva Tolstogo'), ('Maidan Nezalezhnosti', 'Ploshcha Lva Tolstogo')]
G.add_edges_from(intersection_edges)

# Візуалізація графа
    
# Задаємо позиції вузлів для червоної

pos = {
    'Akademmistechko':(-7, 3), 'Zhitimyrska': (-7, 2), 'Sviatishin': (-7, 1),
    'Berestiyska': (-5, 1), 'Shuliavska': (-3, 1), 'Politekhnika': (-1, 1),
    'Vokzalna': (1, 1), 'Universitet': (3, 1), 'Teatralna': (5, 2),
    'Khreschatyk': (7, 2), 'Arsenalna': (9, 2), 'Dnipro': (11, 2),
    'Hidropark': (12, 3), 'Livoberezhna': (13, 4), 'Darnytsia': (14, 5),
    'Chernihivska': (15, 6), 'Lisova': (16, 7)
    }

# Позиції вузлів для другої гілки
pos.update({
    'Syrets': (-1, 5), 'Dorohozhychi': (1, 4), 'Lukianivska': (3, 3), 
    'Zoloti Vorota': (5, 2), 'Palats Sportu': (7, 1), 'Klovska': (9, 0), 
    'Pecherska': (11, -1), 'Druzhby Narodiv': (13, -2), 'Vydubychi': (15, -3)
})

# Позиції вузлів для синьої гілки
pos.update({
    'Minska': (7, 8), 'Obolon': (7, 7), 'Petrovka': (7, 6), 'Tarasa Shevchenko': (7, 5), 
    'Kontraktova Ploshcha': (7, 4), 'Poshtova Ploshcha': (7, 3), 'Maidan Nezalezhnosti': (7, 2), 
    'Ploshcha Lva Tolstogo': (7, 1), 'Olimpiiska': (7, 0), 'Palats Ukraina': (7, -1), 
    'Lybidska': (7, -2), 'Demiivska': (5, -3), 'Holosiivska': (3, -3), 'Vasylkivska': (1, -3),
    'Vystavkovyi Tsentr': (-1, -3), 'Ipodrom': (-3, -3), 'Teremky': (-5, -3)})

# Визначення стартової та кінцевої станції
start_station = 'Lisova'
end_station = 'Teremky'

# Знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
shortest_path = nx.dijkstra_path(G, source=start_station, target=end_station, weight='weight')

# Виведення шляху
print("Найкоротший шлях від станції", start_station, "до станції", end_station, "за алгоритмом Дейкстри:")
print(shortest_path)



# Візуалізація ребер першої гілки
nx.draw_networkx_edges(G, pos, edgelist=connections, width=20.0, alpha=0.8, edge_color='red')

# Візуалізація ребер другої гілки
nx.draw_networkx_edges(G, pos, edgelist=second_branch_connections, width=20.0, alpha=0.8, edge_color='green')

# Візуалізація ребер синьої гілки
nx.draw_networkx_edges(G, pos, edgelist=blue_branch_connections, width=20.0, alpha=0.8, edge_color='blue')


# Візуалізація вузлів з обводкою першої гілки
nx.draw_networkx_nodes(G, pos,
                               nodelist=first_branch_stations,
                               node_color='white',     # колір вузла
                               edgecolors='red',     # колір обводки
                               linewidths=1,           # товщина обводки
                               node_size=500)
# Візуалізація вузлів з обводкою другої гілки
nx.draw_networkx_nodes(G, pos,
                               nodelist=second_branch_stations,
                               node_color='white',     # колір вузла
                               edgecolors='green',     # колір обводки
                               linewidths=1,           # товщина обводки
                               node_size=500)

# Візуалізація вузлів синьої гілки
nx.draw_networkx_nodes(G, pos, 
                                nodelist=blue_branch_stations, 
                                node_color='white', 
                                edgecolors='blue', 
                                linewidths=1, 
                                node_size=500)

# Візуалізація вузлів на перетині гілок
nx.draw_networkx_nodes(G, pos, nodelist=intersection_nodes, node_color='white', node_size=550, edgecolors='black', linewidths=1)

# Створюємо копію позицій для міток
label_pos = pos.copy()

# Ручне зміщення міток для вузлів, що перетинаються
label_pos['Teatralna'] = (pos['Teatralna'][0], pos['Teatralna'][1] - 0.1)
label_pos['Zoloti Vorota'] = (pos['Zoloti Vorota'][0], pos['Zoloti Vorota'][1] + 0.1)
label_pos['Maidan Nezalezhnosti'] = (pos['Maidan Nezalezhnosti'][0], pos['Maidan Nezalezhnosti'][1] - 0.1)
label_pos['Khreschatyk'] = (pos['Khreschatyk'][0], pos['Khreschatyk'][1] + 0.1)
label_pos['Palats Sportu'] = (pos['Palats Sportu'][0], pos['Palats Sportu'][1] - 0.1)
label_pos['Ploshcha Lva Tolstogo'] = (pos['Ploshcha Lva Tolstogo'][0], pos['Ploshcha Lva Tolstogo'][1] + 0.1)

# Візуалізація міток з новими позиціями
nx.draw_networkx_labels(G, label_pos, font_size=5, font_color='black')

# Візуалізація ваг
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                             font_size=6,  # змініть розмір шрифту
                             font_color='black',  # змініть колір шрифту
                             font_family='sans-serif',  # виберіть сімейство шрифту
                             label_pos=0.5)  # змініть положення тексту ваги

# Візуалізація шляху
path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='gray', node_size=50)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=5, alpha=0.5, edge_color='gray')
#nx.draw_networkx_labels(G, pos, labels={node:node for node in shortest_path}, font_color='white')



plt.title('Map of the Kyiv Metro')
plt.axis('off')  # Вимкнення осей
plt.show()


