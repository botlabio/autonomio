import math as m

def shapes( layers, 
            shape, 
            neuron_max,
            neuron_last, 
            dropout):

    neuron_previous = neuron_max
    neuron_count = []
    l = []

    if shape == 'funnel' or shape == 'stairs' and neuron_max - 2 * layers <= 0:

        neuron_count.append(neuron_max)

        for i in range(layers - 1):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i+1]

    if shape == 'rhombus':

        neuron_count.append(1)

        if (layers % 2) == 0:

            n = (layers - 2)/2  #number of layers before or after middle layer

            for i in range(n):
                neuron_count.append(int(neuron_max * (i+1) * 2/layers))

            l = neuron_count[::-1]
            neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])

        else:

            n = (layers - 1) / 2 

            for i in range(n - 1):

                neuron_count.append(int(neuron_max * (3 + 2 * i) / layers))

            l = neuron_count[::-1]
            neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])


    if shape == 'long_funnel':

        n = layers / 2

        for i in range(n):
            neuron_count.append(neuron_max)

        for i in range(n):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i + n]

    if shape == 'brick':

        for i in range(layers):
            neuron_count.append(neuron_max)

    if shape == 'diamond':

        n = layers / 2

        for i in range(n - 1):
            neuron_count.append(int(m.ceil(
                float(neuron_max) * ((float(layers) + i) / 2) / float(layers))))

        neuron_count.append(neuron_max)

        for i in range(n):
            neuron_count.append((neuron_previous + neuron_last) / 2)
            neuron_previous = neuron_count[i + n]

    if shape == 'hexagon':

        print "change2"

        neuron_count.append(1)

        if (layers == 4):
            for i in range(layers - 1):
                neuron_count.append(neuron_max)

        else:

            n = layers / 3

            for i in range(n):
                l.append((neuron_previous + neuron_last) / 2)
                neuron_previous = l[i]

            l = l[::-1]

            if (layers % 3 == 0):

                for i in range(n - 1):
                    neuron_count.append(l[i])

            if (layers % 3 == 1):

                for i in range(n):
                    neuron_count.append(l[i])

            if (layers % 3 == 2):

                for i in range(n):
                    neuron_count.append(l[i])

                neuron_count.append(neuron_max)

            l = l[::-1]

            for i in range(n):
                neuron_count.append(neuron_max)

            for i in range(n):
                neuron_count.append(l[i])

    if shape == 'triangle':

        neuron_count.append(1)

        for i in range(layers - 2):
            l.append((neuron_previous + neuron_last) / 2)
            neuron_previous = l[i]

        l = l[::-1]

        for i in range(layers - 2):
            neuron_count.append(l[i])

        neuron_count.append(neuron_max)

    if shape == 'stairs' and neuron_max - 2 * layers > 0:

        if (layers % 2 == 1):
            neuron_count.append(neuron_max)

        n = layers / 2

        for i in range(n):
            for j in range(2):
                neuron_count.append(neuron_max)
            neuron_max = neuron_max - 2

    print neuron_count

    return neuron_count
